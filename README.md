# All-In-One (AIO) DL

- Python 3 compatible
- Supports all operating systems
- No api keys / credentials required
- Automatically extracts .zip & .rar downloads
- Supports share links from: Google Drive, Dropbox, and Mediafire links


## Usage
```python3
import aiodl as aio

aio.get('https://drive.google.com/file/d/..../view?usp=sharing', './Downloads/')
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
