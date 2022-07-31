# All-In-One (AIO) DL
DOWNLOAD EVERYTHING! - Google Drive, Dropbox, and MediaFire Links

- Python 3 compatible
- Supports all Operating Systems
- NO API KEYS / CREDENTIALS REQUIRED
- Auto Extraction
  - .zip
  - .rar
- Auto Folder & File Naming

## Supported Link Formats
#### Google Drive 

https://drive.google.com/drive/folders/1DhULL2nQJQCAJRa_3VTX2gbAFQJN2OCm?usp=sharing </br>
https://drive.google.com/file/d/1YYMBen3lpvmwTAe1gDVQHkoHtf6KLkgk/view?usp=sharing

#### Dropbox

https://www.dropbox.com/s/e5t94o4yswkl74y/FUTURE%20-%20I%20NEVER%20LIKED%20YOU%20DRUM%20KIT.zip?dl=0
https://www.dropbox.com/s/fnceqyagkkyn36p/%40prodbylewe%20-%20observe%20multikit.zip?dl=1
https://www.dropbox.com/sh/fkpo736kevref7m/AABZk6IFGYqS2aUsXEnFh2i1a?dl=0
https://www.dropbox.com/sh/9h86ddlszfddyuv/AAAUsYEJwSuF0frBlhsfz_GTa?dl=1

#### MediaFire
https://www.mediafire.com/file/vnm6tsqwjw315og/Az3_Music_Library.zip/file


### Usage
```python3
import aiodl as aio

url = 'https://drive.google.com/file/d/1YYMBen3lpvmwTAe1gDVQHkoHtf6KLkgk/view?usp=sharing'
directory = './Downloads/'
aio.get(url, directory)
```
### Bulk Usage
```python3
import aiodl as aio

URL1 = 'https://drive.google.com/file/d/1YYMBen3lpvmwTAe1gDVQHkoHtf6KLkgk/view?usp=sharing'
URL2 = 'https://drive.google.com/drive/folders/1DhULL2nQJQCAJRa_3VTX2gbAFQJN2OCm?usp=sharing'
URL3 = 'https://www.dropbox.com/s/e5t94o4yswkl74y/FUTURE%20-%20I%20NEVER%20LIKED%20YOU%20DRUM%20KIT.zip?dl=0'
URL4 = 'https://www.dropbox.com/sh/9h86ddlszfddyuv/AAAUsYEJwSuF0frBlhsfz_GTa?dl=1'
URL5 = 'https://www.mediafire.com/file/vnm6tsqwjw315og/Az3_Music_Library.zip/file'
bulk_list = [URL1, URL2, URL3, URL4, URL5]
directory = './Downloads/'

for url in bulk_list:
    aio.get(url, directory)
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
