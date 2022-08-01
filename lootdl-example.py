# basic
import aiodl

url = "https://drive.google.com/drive/folders/1DhULL2nQJQCAJRa_3VTX2gbAFQJN2OCm"
location = "./Downloads/"

aiodl.download(url, location)