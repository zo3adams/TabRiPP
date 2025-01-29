# TabRiPP

![TabRiPP Logo](images/logo.jpg)

A simple Python tool to download  Guitar Pro tabs (GP5 format) from a Songsterr URL. The format works with every never version of Guitar pro

---

## Features

- Parses the numeric Songsterr **ID** from a link like:  
  `https://www.songsterr.com/a/wsa/<some-artist-or-song>-tab-s12345`
- Downloads the latest **Guitar Pro** file for that ID.
- Saves the file to a directory you specify.

---

## Requirements

- Python 3.7+ (though it should work on most modern versions)
- `requests`
- `tqdm`

Install Python packages (if you haven’t already):
```bash
pip install requests tqdm
```

## Usage
Clone or copy this repository (and ensure you have the script, e.g. downloader.py).
Run the script from the command line, specifying the Songsterr link and (optionally) a download directory:
```bash
python downloader.py "https://www.songsterr.com/a/wsa/artist-song-tab-s12345" --download-dir .
```
The first argument must be the Songsterr link (the one ending in -s<id>).
Use 
```bash
--download-dir YOUR_DIRECTORY
```
 if you want to specify somewhere else to save the file.

Example:

```bash
python downloader.py "https://www.songsterr.com/a/wsa/a-_-tab-s489524" --download-dir "C:/Users/YourName/Desktop/Tabs"
```
