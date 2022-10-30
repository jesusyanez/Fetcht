# LootDL

## API-less download library for <a href="https://www.google.com/drive/">Google Drive</a>, <a href="https://www.dropbox.com/">Dropbox</a>, <a href="https://www.mediafire.com/">MediaFire</a>, and <a href="https://wetransfer.com/">WeTransfer</a>.

<img src="https://github.com/jesusyanez/example-images/blob/main/downloader-example.gif?raw=true" />


- Python 3 
- Works on all operating systems
- No API keys / credentials needed
- Auto extracts .zip files
- Auto extracts .rar files (requires 7zip)
- Auto deletes compressed files after extraction



## Usage
```python3
import lootdl

url = "https://drive.google.com/file/d/.../view?usp=sharing"
download_path = "./Downloads/"

lootdl.grab(url, download_path)
```

### Bulk Usage
```python3
import lootdl

download_list = ['URL1', 'URL2', 'URL3']
download_path = "./"

for url in download_list:
 lootdl.grab(url, download_path)
```

## Supported URL Formats

Google Drive
```txt
https://drive.google.com/drive/folders/...?usp=sharing
https://drive.google.com/file/d/.../view?usp=sharing
```
Dropbox
```txt
https://www.dropbox.com/s/.../...?dl=0
https://www.dropbox.com/s/.../...?dl=1
https://www.dropbox.com/sh/.../...?dl=0
https://www.dropbox.com/sh/.../...?dl=1
```
MediaFire
```txt
https://www.mediafire.com/file/.../.../file
```
WeTransfer
```txt
https://wetransfer.com/downloads/.../...
```


## Roadmap
- [X] Google Drive
- [X] Dropbox
- [X] MediaFire
- [X] WeTransfer
- [ ] Mega
 
 ## Acknowledgements 
 
Thank you to the authors of the following repos:
- "gdrivedl" by matthuisman - https://github.com/matthuisman/gdrivedl
- "mediafire-dl" by Juvenal-Yescas - https://github.com/Juvenal-Yescas/mediafire-dl
- "transferwee" by iamleot - https://github.com/iamleot/transferwee
