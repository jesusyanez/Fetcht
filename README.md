# All-In-One (AIO) DL

- Python 3 compatible
- Supports all operating systems
- No api keys / CREDENTIALS REQUIRED
- Downloads from:
  - Google Drive
  - Dropbox
  - MediaFire
- Automatically extracts folders
  - .zip
  - .rar

## Usage
```python3
import aiodl as aio

aio.get('https://drive.google.com/file/d/..../view?usp=sharing', './Downloads/')
```
### Bulk Downloads
```python3
import aiodl as aio

list = [URL1, URL2, URL3]
directory = './Downloads/'

for url in list:
    aio.get(url, directory)
```

## Supported Links
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


## Roadmap
- [X] Google Drive
- [X] Dropbox
- [X] MediaFire
- [ ] Mega
 
## Acknowledgments
Inspired by & uses:<br/>
https://github.com/matthuisman/gdrivedl <br/>
https://github.com/Juvenal-Yescas/mediafire-dl
