# This file is an All-In-One module for downloading from cloud storage services
# Supports share links from Google Drive, Dropbox, MediaFire, and WeTransfer
# Does not use any APIs
# Thank you to the authors of the following repos:
#   "gdrivedl" by matthuisman - https://github.com/matthuisman/gdrivedl
#   "mediafire-dl" by Juvenal-Yescas - https://github.com/Juvenal-Yescas/mediafire-dl
#   "transferwee" by iamleot - https://github.com/iamleot/transferwee

import gdrivedl
import mediafiredl
import wetransferdl
import mediafire_request
import os
import requests
import zipfile
import patoolib
from bs4 import BeautifulSoup

# define urls to filter cloud service
gdrive_url = 'drive.google.com'
dropbox_url = 'dropbox.com'
mediafire_url = 'mediafire.com'
wetransfer_url = 'wetransfer.com'

# Google drive folder link url downloader
def download_folder(url, output_folder, filename=None):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename=None)

# Google drive file link url downloader
def download_file(url, output_folder, filename):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename)

# Gets file/folder title with requests
def get_title(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text()

# Gets mediafire file/folder title with requests
def get_title_mf(url):
    reqs = mediafire_request.get_mediafire(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    temp_output = str(soup.find('div', {'class': 'filename'}).get_text())
    return temp_output

# Detects file compression type
def compression_type(file_name):
    ext = os.path.splitext(file_name)[-1].lower()
    print(ext)
    return ext

# Uncompresses files and then deletes compressed folder
def unzip(zipped_file, unzipped_file, directory):
    if compression_type(zipped_file) == '.zip':
        zip_path = directory + zipped_file
        unzip_path = directory + unzipped_file
        print('--> Extracting to: ' + unzip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                zip_ref.close()
        os.remove(zip_path)
    if compression_type(zipped_file) == '.rar':
        zip_path = directory + zipped_file
        unzip_path = directory + unzipped_file
        print('---> Extracting to: ' + unzip_path)
        patoolib.extract_archive(zip_path, outdir=directory)
        os.remove(zip_path)
    return

# Download from Google Drive
def gd_download(url, directory):
    if 'folder' in url:
        output = get_title(url)[:-15]
        output_path = directory + output
        print("---> Downloading to: " + output_path)
        download_folder(url, output_path)
    elif 'file' in url:
        temp_output = get_title(url)[:-15]
        output = temp_output.split('.', 1)[0]
        print("---> Downloading to: " + directory + temp_output)
        download_file(url, directory, temp_output)
        unzip(temp_output, output, directory)
    else: 
        print('The url: '+ url + ' is not supported, sorry.')

# Download from Dropbox
def db_download(url, directory):
    url = url[:-1] + '0'
    file_name = get_title(url)[:-21][10:]
    print(file_name)
    suffix1 = file_name.endswith(".zip")
    suffix2 = file_name.endswith(".rar")
    print(suffix1)
    print(suffix2)
    if not suffix1 and not suffix2:
        file_name = file_name + ".zip"
    dl_url = url[:-1] + '1'
    filepath = directory + file_name
    print("---> Downloading to: " + filepath)
    output = file_name[:-4]
    headers = {'user-agent': 'Wget/1.16 (linux-gnu)'}
    r = requests.get(dl_url, stream=True, headers=headers)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    unzip(file_name, output, directory)

# Download from MediaFire
def mf_download(url, directory):
    zip_name = get_title_mf(url)
    temp_output = directory + zip_name
    print('---> Downloading to: ' + temp_output)
    output = zip_name[:-4]
    mediafiredl.download(url, temp_output, quiet=True)
    unzip(zip_name, output, directory)

# Download from WeTransfer
def wt_download(url, directory):
    wetransferdl.download(url, directory, extract=True)

# Detects url cloud service type and downloads it to a specific location
def grab(url, output_path):
    if gdrive_url in url:
        gd_download(url, output_path)
    if dropbox_url in url:
        db_download(url, output_path)
    if mediafire_url in url:
        mf_download(url, output_path)
    if wetransfer_url in url:
        wt_download(url, output_path)