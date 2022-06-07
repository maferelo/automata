import subprocess

from spotipy.client import Spotify
from typing import List

import config

from globals import spotipy_session
from globals import logger

def get_playlists_urls(spotipy_session: Spotify, spotify_username: str) -> List[str]:
    playlists_urls = []
    playlists = spotipy_session.user_playlists(spotify_username)
    while playlists:
        playlists_urls.extend(playlist['external_urls']['spotify'] for playlist in playlists['items'])
        playlists = spotipy_session.next(playlists) if playlists['next'] else None
    return playlists_urls

def download_playlists(download_directory: str, playlists_urls: List[str]) -> None:
    subprocess.run(f'cd {download_directory}', shell=True)
    for playlist in playlists_urls:
        logger.info(f'Downloading {playlist}')
        output = subprocess.check_output(f'spotdl {playlist}', shell=True)
        logger.info(f'Output {output}')
        break

def main() -> None:
    playlists_urls = get_playlists_urls(spotipy_session, config.SPOTIFY_USERNAME)
    download_playlists(config.DOWNLOADS_DIRECTORY, playlists_urls)

if __name__ == '__main__':
    main()