#!/bin/bash
apt-get update -y

apt-get upgrade -y

sudo apt-get install -y \
    exfat-fuse \
    exfat-utils \
    git \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    openssl \
    ;

curl -fsSL https://get.docker.com -o get-docker.s
sh get-docker.sh

cp .env.example .env

sudo docker compose -f docker-compose.rpi.yml up

curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install 3.8.13
pyenv virtualenv venv
pyenv global venv
pyenv activate venv
echo "export PYENV_ROOT=$HOME/.pyenv" >> ~/.bashrc
echo "command -v pyenv >/dev/null || export PATH=$PYENV_ROOT/bin:$PATH" >> ~/.bashrc
echo "eval $(pyenv init -)" >> ~/.bashrc
echo "eval $(pyenv virtualenv-init -)" >> ~/.bashrc

curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc

poetry config virtualenvs.create false
poetry install
