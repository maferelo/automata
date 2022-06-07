import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME") or ""
DOWNLOADS_DIRECTORY = os.environ.get("DOWNLOADS_DIRECTORY") or ""
