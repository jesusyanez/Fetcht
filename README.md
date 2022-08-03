# All-In-One (AIO) DL

- Python 3 
- Works on all operating systems
- No API keys / credentials needed
- Downloads from Google Drive, Dropbox, Mediafire, and WeTransfer
- Automatically extracts, then deletes .zip & .rar files

## Usage
```python3
import aiodl

# aiodl.download(url, download location)
aiodl.download('https://drive.google.com/file/d/.../view?usp=sharing', './Downloads/')
```
Ensure the download location exists and ends with a "/" or it may cause issues. You can use "./" to download to the working directory.

## Download URL Formats
```txt
Google Drive
https://drive.google.com/drive/folders/...?usp=sharing
https://drive.google.com/file/d/.../view?usp=sharing

Dropbox
https://www.dropbox.com/s/.../...?dl=0(1)
https://www.dropbox.com/sh/.../...?dl=0(1)

MediaFire
https://www.mediafire.com/file/.../.../file

WeTransfer
https://wetransfer.com/downloads/.../...
```


## Roadmap
- [X] Google Drive
- [X] Dropbox
- [X] MediaFire
- [X] WeTransfer
- [ ] Mega
 
