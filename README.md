# Automata

> Several personal scripts for automation of everyday of tasks
> using best practices with reference notes.

## Prerequisites

Install requirements: [ex-fuse](https://packages.debian.org/source/buster/fuse-exfat), [Python3.9.13](https://www.python.org/), [Docker](https://www.docker.com/).

For linux:

```bash
sudo sh install-requirements.sh
```

## Installation using Docker Compose

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata
docker-compose build
```

## Running the services

```bash
docker-compose up
docker-compose logs -f
```

## Local development environment

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

TELEGRAM_CHAT_ID=

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
