from typing import List
import logging
import os.path
import re
import urllib.parse
import zlib
import requests
import zipfile

WETRANSFER_API_URL = 'https://wetransfer.com/api/v4/transfers'
WETRANSFER_DOWNLOAD_URL = WETRANSFER_API_URL + '/{transfer_id}/download'

WETRANSFER_DEFAULT_CHUNK_SIZE = 5242880
WETRANSFER_EXPIRE_IN = 604800

logger = logging.getLogger(__name__)


def download_url(url: str) -> str:
    """Given a wetransfer.com download URL download return the downloadable URL.
    The URL should be of the form `https://we.tl/' or
    `https://wetransfer.com/downloads/'. If it is a short URL (i.e. `we.tl')
    the redirect is followed in order to retrieve the corresponding
    `wetransfer.com/downloads/' URL.
    The following type of URLs are supported:
     - `https://we.tl/<short_url_id>`:
        received via link upload, via email to the sender and printed by
        `upload` action
     - `https://wetransfer.com/<transfer_id>/<security_hash>`:
        directly not shared in any ways but the short URLs actually redirect to
        them
     - `https://wetransfer.com/<transfer_id>/<recipient_id>/<security_hash>`:
        received via email by recipients when the files are shared via email
        upload
    Return the download URL (AKA `direct_link') as a str or None if the URL
    could not be parsed.
    """
    logger.debug(f'Getting download URL of {url}')
    # Follow the redirect if we have a short URL
    if url.startswith('https://we.tl/'):
        r = requests.head(url, allow_redirects=True)
        logger.debug(f'Short URL {url} redirects to {r.url}')
        url = r.url

    recipient_id = None
    params = urllib.parse.urlparse(url).path.split('/')[2:]

    if len(params) == 2:
        transfer_id, security_hash = params
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return None

    logger.debug(f'Getting direct_link of {url}')
    j = {
        "intent": "entire_transfer",
        "security_hash": security_hash,
    }
    if recipient_id:
        j["recipient_id"] = recipient_id
    s = _prepare_session()
    r = s.post(WETRANSFER_DOWNLOAD_URL.format(transfer_id=transfer_id),
               json=j)

    j = r.json()
    return j.get('direct_link')


def _file_unquote(file: str) -> str:
    """Given a URL encoded file unquote it.
    All occurences of `\', `/' and `../' will be ignored to avoid possible
    directory traversals.
    """
    return urllib.parse.unquote(file).replace('../', '').replace('/', '').replace('\\', '')


def download(url: str, directory: str, extract: bool, file: str = '') -> None:
    """Given a `we.tl/' or `wetransfer.com/downloads/' download it.
    First a direct link is retrieved (via download_url()), the filename can be
    provided via the optional `file' argument. If not provided the filename
    will be extracted to it and it will be fetched and stored on the current
    working directory.
    """
    logger.debug(f'Downloading {url}')
    dl_url = download_url(url)
    if not file:
        file = _file_unquote(urllib.parse.urlparse(dl_url).path.split('/')[-1])

    temp_output = directory + file

    print('---> Downloading to: ' + temp_output)
    logger.debug(f'Fetching {dl_url}')
    r = requests.get(dl_url, stream=True)
    with open(temp_output, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
    
    if extract:
        unzip_path = directory + os.path.splitext(file)[0]
        print('--> Extracting to: ' + unzip_path)
        with zipfile.ZipFile(temp_output, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                zip_ref.close()
        os.remove(temp_output)


def _prepare_session() -> requests.Session:
    """Prepare a wetransfer.com session.
    Return a requests session that will always pass the required headers
    and with cookies properly populated that can be used for wetransfer
    requests.
    """
    s = requests.Session()
    r = s.get('https://wetransfer.com/')
    m = re.search('name="csrf-token" content="([^"]+)"', r.text)
    s.headers.update({
        'x-csrf-token': m.group(1),
        'x-requested-with': 'XMLHttpRequest',
    })

    return s