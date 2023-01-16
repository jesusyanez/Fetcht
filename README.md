# CDL

#### <p><i>1 package, 4 providers, 0 APIs</i></p>

<img src="https://github.com/jesusyanez/example-images/blob/main/downloader-example.gif?raw=true" />

- Python 3
- Works on all operating systems
- No API keys / credentials needed
- Auto extracts .zip files
- Auto extracts .rar files (requires 7zip)
- Removes compressed files after extraction

## Supported URLs

```txt
# Google Drive
https://drive.google.com/drive/folders/...?usp=sharing
https://drive.google.com/file/d/.../view?usp=sharing

# Dropbox
https://www.dropbox.com/s/.../...?dl=0(1)
https://www.dropbox.com/sh/.../...?dl=0(1)

# MediaFire
https://www.mediafire.com/file/.../.../file

# WeTransfer
https://wetransfer.com/downloads/.../...
```

## Usage

```python3
import cdl

download_list = ["URL1", "URL2", "URL3"]
download_path = "./"

for url in download_list:
 cdl.grab(url, download_path)
```

## Roadmap

- [x] Google Drive
- [x] Dropbox
- [x] MediaFire
- [x] WeTransfer
- [ ] Mega

## Acknowledgement

Code was borrowed from <a href="https://github.com/matthuisman/gdrivedl">gdrivedl</a>, <a href="https://github.com/Juvenal-Yescas/mediafire-dl">mediafire-dl</a>, and <a href="https://github.com/iamleot/transferwee">transferwee</a> to create lootdl.
