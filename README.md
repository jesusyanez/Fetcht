# All-In-One (AIO) DL
DOWNLOAD EVERYTHING! - Google Drive, Dropbox, and MediaFire Links

- Python 3 compatible
- Supports all Operating Systems
- NO API KEYS / CREDENTIALS REQUIRED
- Auto Folder & File Naming
- Auto Extraction
  - .zip
  - .rar

## Supported Link Formats
```txt
Google Drive
https://drive.google.com/drive/folders/..?usp=sharing
https://drive.google.com/file/d/..../view?usp=sharing

Dropbox
https://www.dropbox.com/s/........./.........zip?dl=0
https://www.dropbox.com/s/........./.........zip?dl=1
https://www.dropbox.com/sh/............/........?dl=0
https://www.dropbox.com/sh/............/........?dl=1

MediaFire
https://www.mediafire.com/file/...../........zip/file
```
## Usage
```python3
import aiodl as aio

url = 'https://drive.google.com/file/d/..../view?usp=sharing'
directory = './Downloads/'

aio.get(url, directory)
```
### Bulk Downloads
```python3
import aiodl as aio

URL1 = 'https://drive.google.com/file/d/..../view?usp=sharing'
URL2 = 'https://www.dropbox.com/sh/............/........?dl=0'
URL3 = 'https://www.mediafire.com/file/...../........zip/file'

list = [URL1, URL2, URL3]
directory = './Downloads/'

for url in list:
    aio.get(url, directory)
```

## Roadmap
- [X] Google Drive
- [X] Dropbox
- [X] MediaFire
- [ ] Mega
 
## Acknowledgments
Inspired by & uses:<br/>
https://github.com/matthuisman/gdrivedl <br/>
https://github.com/Juvenal-Yescas/mediafire-dl
