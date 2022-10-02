# Automata

> Personal scripts for automation of everyday tasks
> using best practices with reference notes.

## Prerequisites

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata
```

### For Mac

* [Docker](https://www.docker.com/)
* [Homebrew](https://brew.sh/)

```bash
bash scripts/prestart-mac.sh
```

### For RaspberryPi

* [Docker](https://www.docker.com/)
* [ex-fuse](https://packages.debian.org/source/buster/fuse-exfat)
* [Pyenv](https://github.com/pyenv/pyenv)
* [Python3.8.13](https://www.python.org/)

```bash
ssh pi@192.168.1.3
sudo bash scripts/prestart-rpi.sh
```

## Development

We use [remote containers](https://code.visualstudio.com/docs/remote/containers-tutorial).

1. Press F1 to open the Command Palette.
2. Type reopen in container.
3. Select Remote Containers: Reopen in Container from the list of available options.

Inside the container run:

```bash
uvicorn app.main:app --host 0.0.0.0 --reload
```

Check the endpoint

```bash
curl --location --request GET 'http://localhost:8000/'
```

### Linting

```bash
pre-commit run --all-files
```

### Dependencies

Use the package manager [poetry](https://python-poetry.org/) to install requirements

```bash
poetry add <package>
```

### Database migrations

Using [Alembic](https://alembic.sqlalchemy.org/en/latest/)

Change models and commit

```bash
alembic revision --autogenerate -m "<message>"
alembic upgrade head
```

### Rpi

```bash
docker compose -f docker-compose.rpi.yml up
```

## Deployments

Using [Heroku](https://python-poetry.org/)

```bash
heroku login
git push heroku main
heroku open
heroku logs --tail
```

## Usage RaspberryPi app

### Features

* reset_jobs: Set the scripts to run consecutive by day of month.

### Scripts

* update: Update the rpi
* cleanup: Clean after reboot from update
* backup: Clone rpi to hdd

### Runnning the app

```bash
sudo bash scripts/prestart-rpi.sh
```

## References

* [Project homepage](https://your.github.com/automata/)
* [Repository](https://github.com/maferelo/automata/)
* [Issue tracker](https://github.com/your/maferelo/issues)
  * In case of sensitive bugs like security vulnerabilities, please contact
    maferelo13@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
* Related projects
  * Your other project
  * Someone else's project
  * [Awesome README](https://github.com/matiassingers/awesome*readme)
