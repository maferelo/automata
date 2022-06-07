import spotipy

import logs

auth_manager = spotipy.oauth2.SpotifyClientCredentials()
spotipy_session = spotipy.Spotify(auth_manager=auth_manager)

logger = logs.create_logger()
