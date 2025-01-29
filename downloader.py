import re
import sys
import json
import argparse
import requests
from tqdm import tqdm
from pathlib import Path

def download_songsterr_link(songsterr_link, download_dir):
    """
    Given a full Songsterr link like:
      'https://www.songsterr.com/a/wsa/artist-song-tab-s12345'
    download the latest available Guitar Pro file (GPX, GP5, etc.).
    """


    match = re.search(r"s(\d+)$", songsterr_link.strip())
    if not match:
        print(f"Could not parse Songsterr ID from link: {songsterr_link}")
        return

    song_id = match.group(1)


    revisions_url = f"https://www.songsterr.com/api/meta/{song_id}/revisions"
    try:
        resp = requests.get(revisions_url)
    except Exception as e:
        print(f"Error fetching revisions data for song ID {song_id}: {e}")
        return

    if resp.status_code != 200:
        print(f"Songsterr API returned status code {resp.status_code} for {revisions_url}")
        return

    revisions = resp.json()
    if not revisions:
        print(f"No revisions found for song ID {song_id}")
        return


    latest_revision = revisions[0]
    source_url = latest_revision.get('source')
    if not source_url:
        print(f"No 'source' found in the latest revision for song ID {song_id}")
        return

 
    download_dir_path = Path(download_dir).expanduser()
    download_dir_path.mkdir(parents=True, exist_ok=True)


    extension = source_url.rsplit('.', 1)[-1]
    filename = download_dir_path / f"Song_{song_id}.{extension}"

    print(f"\nFound tab for Songsterr ID {song_id} — saving as {filename}\n")


    try:
        file_resp = requests.get(source_url, stream=True)
    except Exception as e:
        print(f"Error downloading file from {source_url}: {e}")
        return

    if file_resp.status_code != 200:
        print(f"Failed to download {source_url}, got status code {file_resp.status_code}")
        return

    total_size = int(file_resp.headers.get('content-length', 0))
    with open(filename, 'wb') as f, tqdm(
        total=total_size, unit='B', unit_scale=True, desc="Downloading"
    ) as pbar:
        for chunk in file_resp.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)
                pbar.update(len(chunk))

    print(f"Download complete: {filename}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Download the Guitar Pro tab (GPX/GP5) from a Songsterr link."
    )
    parser.add_argument(
        "link",
        help="Songsterr link ending with '-s12345' (e.g. https://www.songsterr.com/a/wsa/metallica-nothing-else-matters-tab-s12345)"
    )
    parser.add_argument(
        "--download-dir",
        default="~/Tabs",
        help="Where to save the downloaded file (default: ~/Tabs)"
    )

    args = parser.parse_args()


    download_songsterr_link(args.link, args.download_dir)

if __name__ == "__main__":
    main()
