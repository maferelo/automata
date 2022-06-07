# Apps

> Several personal scripts for automation of everyday of tasks.

## Install

Install [ffmpeg](https://ffmpeg.org/) to enable audio streaming for spotify-downloader package.

```bash
brew install ffmpeg
sudo apt get install ffmpeg
```

Use the package manager [poetry](https://python-poetry.org/) to install requirements.

```bash
poetry install
```

### Initial Configuration

Spotipy.

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

Use .env file to setup the apps configuration

DOWNLOADS_DIRECTORY

Path to donwloads e.g. '/Volumes/SDCard/Downloads'

SPOTIFY_USERNAME

User to extract data from e.g. '12125368756'

## Usage

```bash
poetry shell
cd apps/
```

Download spotify playlist with yt-download

```bash
python spotify_dl.py
```

## Features

- spotify_dl: Download spotify playlist with yt-download

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Links

- Project homepage: https://your.github.com/apps/
- Repository: https://github.com/maferelo/apps/
- Issue tracker: https://github.com/your/maferelo/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    maferelo13@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project:
  - Someone else's project:
  - Awesome README: https://github.com/matiassingers/awesome-readme
