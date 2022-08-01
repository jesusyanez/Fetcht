# All-In-One (AIO) DL

- Python 3 compatible
- Supports all operating systems
- No API keys / credentials required
- Automatically names folders
- Automatically extracts then deletes .zip & .rar files
- Supports share links from: Google Drive, Dropbox, and MediaFire

## Usage
```python3
import aiodl

# aiodl.download(url, download location)
aiodl.download('https://drive.google.com/file/d/.../view?usp=sharing', './Downloads/')
```

## Supported Links
```txt
Google Drive
https://drive.google.com/drive/folders/...?usp=sharing
https://drive.google.com/file/d/.../view?usp=sharing

Dropbox
https://www.dropbox.com/s/.../...?dl=0
https://www.dropbox.com/s/.../...?dl=1
https://www.dropbox.com/sh/.../...?dl=0
https://www.dropbox.com/sh/.../...?dl=1

MediaFire
https://www.mediafire.com/file/.../.../file
```


## Roadmap
- [X] Google Drive
- [X] Dropbox
- [X] MediaFire
- [ ] WeTransfer
- [ ] Mega
 
## Acknowledgments
Inspired by & uses modified versions of:<br/>
https://github.com/matthuisman/gdrivedl <br/>
https://github.com/Juvenal-Yescas/mediafire-dl
