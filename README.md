# LootDL

#### <p> A cloud storage downloader.</p>
<p> Google Drive | MediaFire | DropBox | WeTransfer</p>

## Requirements
- [Python 3](https://www.python.org/downloads/)
- Windows or Linux
- Downloads from share links.


## Usage

```python3
import cdl

cdl.grab(<URL>, <OUTPUT_FOLDER_PATH>)
```

## Links

```txt
Google Drive
------------------------------------------------------------
https://drive.google.com/drive/folders/example?usp=sharing
https://drive.google.com/file/d/example/view?usp=sharing

Dropbox
------------------------------------------------------------
https://www.dropbox.com/s/example/example?dl=0(1)
https://www.dropbox.com/sh/example/example?dl=0(1)

MediaFire
------------------------------------------------------------
https://www.mediafire.com/file/example/example/file

WeTransfer
------------------------------------------------------------
https://wetransfer.com/downloads/example/example

```


## Acknowledgement

Code was borrowed from <a href="https://github.com/matthuisman/gdrivedl">gdrivedl</a>, <a href="https://github.com/Juvenal-Yescas/mediafire-dl">mediafire-dl</a>, and <a href="https://github.com/iamleot/transferwee">transferwee</a> to create lootdl.
