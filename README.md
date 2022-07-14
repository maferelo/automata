# Automata

> Several personal scripts for automation of everyday of tasks
> using best practices with reference notes.

## Prerequisites

Install requirements: [ex-fuse](https://packages.debian.org/source/buster/fuse-exfat), [Python3.8.13](https://www.python.org/), [Docker](https://www.docker.com/), [Pyenv](https://github.com/pyenv/pyenv).

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata
```

#### For linux:

```bash
sudo sh start-raspberry.sh
```

#### For Mac

Install [Homebrew](https://brew.sh/).

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Development

We use [Remote containers](https://code.visualstudio.com/docs/remote/containers-tutorial).

1. Press F1 to open the Command Palette.
2. Type reopen in container.
3. Select Remote Containers: Reopen in Container from the list of available options.

Inside the container run:

```bash
uvicorn app.main:app --host 0.0.0.0 --reload
```

visit https://localhost:8000/

## Installation using Docker Compose

```bash
cd automata
docker-compose build
```

### Running the services

Local

```bash
docker-compose up
docker-compose logs -f
```

On the rpi

```bash
docker-compose -f docker-compose.rpi.yml build
docker-compose -f docker-compose.rpi.yml up
```

## Local development environment

### Intall python

Add the following to .bash_profile so that you can hit pyenv.

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Reload .bash_profile.

```bash
source ~/.bash_profile
```

```bash
pyenv install 3.8.13
```

Change the version.

```bash
pyenv global 3.8.13
```

Use the package manager [poetry](https://python-poetry.org/) to install requirements.

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry install
```

### Initial Configuration

Use .env file to setup the Automata configuration

SCHELUDER_SCRIPTS

Name of files to run in the scripts directory e.g. "update,cleanup,backup"

TELEGRAM_TOKEN

TELEGRAM_CHAT_ID

TZ

Timezone for the project (optional) e.g. "America/Bogota"

## Usage

```bash
poetry shell
python automata/main.py --help
```

## Features

- reset_jobs: Set the scripts to run consecutive by day of month.

### Scripts

- update: Update the rpi
- cleanup: Clean after reboot from update
- backup: Clone rpi to hdd

## Deployments

Using [Heroku](https://python-poetry.org/)

```bash
heroku login
```

To create an app

```bash
heroku create -a automata
heroku stack:set container
```

To connecto to an existing app

```bash
git push heroku main
heroku open
heroku logs --tail
```

## Links

- Project homepage: https://your.github.com/automata/
- Repository: https://github.com/maferelo/automata/
- Issue tracker: https://github.com/your/maferelo/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    maferelo13@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project:
  - Someone else's project:
  - Awesome README: https://github.com/matiassingers/awesome-readme
