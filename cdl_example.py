import cdl

URL1 = 'https://drive.google.com/file/d/10AobmWPeTkxSakayl_KMWyW49vWykfOv/view?usp=drivesdk'
URL2 = 'https://drive.google.com/file/d/10qzS3QC4hd8ZooddDJAwjP1WZeLkJJE7/view'
URL3 = 'https://drive.google.com/drive/folders/1BeDSsn8CzHH7ooIsm2s7EqgwDVWvFDuY'
URL4 = 'https://www.mediafire.com/file/m14lgmko672qmxx/#maknae2021.zip/file'
URL5 = 'https://drive.google.com/file/d/11Qwdfj-5RacRROV3elBW712CS3vEo-53/view?usp=sharing'

download_list = [URL1, URL2, URL3, URL4, URL5]

for url in download_list:
 cdl.grab(url, './')