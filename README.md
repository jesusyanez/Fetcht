# FinesseDL
DOWNLOAD EVERYTHING! - Google Drive, Dropbox, and MediaFire Links

- Python 3 compatible
- Supports all Operating Systems
- NO API Keys Required
- Auto Extraction
  - .zip
  - .rar ([7z installation required](https://www.7-zip.org/download.html))
- Autonames downloads

### Usage
```python3
import finessedl as fdl

# finessedl.download(url, output_folder)
fdl.get('drive.google.com/fsdlfks', './Downloads')

```
#### List Usage
```python3
import finessedl as fdl

dl_list = ['drive.google.com/fsdlfks', 'mediafire.com/file/fsjkldfls', 'dropbox.com/s/fjklsdfjl434']
output_folder = './Downloads'

for url in dl_list:
    fdl.get(url, output_folder)

```

## Supported Links
- [X] Google Drive
- [X] Dropbox
- [ ] MediaFire
- [ ] Mega
 
## Acknowledgments
Scripts used:<br/>
[gdrivedl](https://github.com/matthuisman/gdrivedl)
