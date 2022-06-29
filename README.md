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

## Installation using Docker Compose

```bash
cd automata
docker-compose build
```

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

## Local development environment

Use the package manager [poetry](https://python-poetry.org/) to install requirements.

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry install
```

## Running the services

```bash
docker-compose up
docker-compose logs -f
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

- update: Update the raspberrypi
- cleanup: Clean after reboot from update
- backup: Clone rpi to hdd

## Deployments using [Heroku](https://python-poetry.org/)

```bash
heroku create -a automata
heroku addons:create heroku-postgresql:hobby-dev --version=14
heroku container:login
heroku container:push web
heroku container:release web
heroku open
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
