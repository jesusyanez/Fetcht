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

# lootdl.download(url, output_directory)
lootdl.get('https://drive.google.com/file/d/fs4lf234ks1/view?usp=sharing', './Downloads')

```
#### List Usage
```python3
import lootdl

list = ['Dropbox_URL', 'MediaFire_URL', 'Google_Drive_URL']
output_folder = './Downloads' #Make sure output directory exists before running

for url in list:
    lootdl.get(url, output_folder)

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
