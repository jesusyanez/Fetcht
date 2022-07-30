import gdrivedl
import os
import requests
import pathlib
import zipfile
import patoolib
import mediafireDL
from bs4 import BeautifulSoup

def download_folder(url, output_folder, filename=None):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename=None)

def download_file(url, output_folder, filename):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename)

def get_title(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text() #[:-15]

def get_title_mf(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    temp_output = str(soup.find('div', {'class': 'filename'}).get_text())
    return temp_output
    # output = temp_output[:-4]

def compression_type(file_name):
    file_extension = pathlib.Path(file_name).suffix.lower()
    return file_extension

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

gdrive_url = 'drive.google.com'
dropbox_url = 'dropbox.com'
mediafire_url = 'mediafire.com'

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

def db_download(url, directory):
    url = url[:-1] + '0'
    file_name = get_title(url)[:-21][10:]
    suffix1 = file_name.endswith(".zip")
    suffix2 = file_name.endswith(".rar")
    if not suffix1 or not suffix2:
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

def mf_download(url, directory):
    zip_name = url[:-5].rsplit('/', 1)[-1]
    temp_output = directory + zip_name
    print('---> Downloading to: ' + temp_output)
    output = zip_name[:-4]
    mediafireDL.download(url, temp_output, quiet=True)
    unzip(zip_name, output, directory)

def grab(url, output_path):
    if gdrive_url in url:
        gd_download(url, output_path)
    if dropbox_url in url:
        db_download(url, output_path)
    if mediafire_url in url:
        mf_download(url, output_path)