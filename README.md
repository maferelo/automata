# Automata

> Several personal scripts for automation of everyday of tasks
> using best practices with reference notes.

## Install

Install requirements: [ex-fuse](https://packages.debian.org/source/buster/fuse-exfat), [Python3.9.13](https://www.python.org/), [Docker](https://www.docker.com/).

```bash
sudo sh install-requirements.sh
```

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata/
```

Use the package manager [poetry](https://python-poetry.org/) to install requirements.

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry install
```

### Initial Configuration

Use .env file to setup the Automata configuration

TZ

Timezone for the project (optional) e.g. 'America/Bogota'

## Usage

```bash
poetry shell
python automata/main.py --help
```

## Features

- reset_jobs: Set the cronjobs to run consecutive by day of month.

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

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
