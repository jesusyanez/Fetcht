# LootDL
DOWNLOAD EVERYTHING! - Google Drive, Dropbox, and MediaFire Links

- Python 3 compatible
- Supports all Operating Systems
- NO API KEYS
- Auto Extraction
  - .zip
  - .rar
- Auto File Naming

### Supported Link Types
```txt
Dropbox

'https://www.dropbox.com/s/.../example.zip?dl=0'
'https://www.dropbox.com/s/.../example.zip?dl=1'
'https://www.dropbox.com/sh/.../...?dl=0'
'https://www.dropbox.com/sh/.../...?dl=1'  

Google Drive

'https://drive.google.com/drive/folders/...?usp=sharing'
'https://drive.google.com/file/d/.../view?usp=sharing'

MediaFire

'https://www.mediafire.com/file/.../example.zip/file'
```

### Usage
```python3
import lootdl

# lootdl.grab(url, directory)
lootdl.grab('URL', './')
```
### In a list
```python3
import lootdl

#Make sure output directory exists before running
directory = './Downloads/'
list = ['URL1', 'URL2', 'URL3']

for url in list:
    lootdl.grab(url, directory)
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
