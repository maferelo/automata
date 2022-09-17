#!/bin/bash
docker-compose -f docker-compose.rpi.yml build

docker-compose -f docker-compose.rpi.yml up

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
source "$HOME/.bashrc"
pyenv install 3.8.13
pyenv global 3.8.13
