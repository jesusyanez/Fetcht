# All-In-One (AIO) DL

- Works with Python 3 
- Works on Windows & Linux
- No API keys / credentials needed
- Automatically names folders
- Automatically extracts then removes .zip & .rar files
- Supports Google Drive, Dropbox, MediaFire, WeTransfer, and more coming soon

## Usage
```python3
import aiodl

# aiodl.download(url, download location)
aiodl.download('https://drive.google.com/file/d/.../view?usp=sharing', './Downloads/')
```
Ensure the download location exists and ends with a "/" or it will cause issues. You can use "./" to download to the working directory.

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
 
## Acknowledgments
Inspired by & uses modified versions of:<br/>
https://github.com/matthuisman/gdrivedl <br/>
https://github.com/Juvenal-Yescas/mediafire-dl <br/>
https://github.com/iamleot/transferwee
