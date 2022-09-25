#!/bin/bash
set +u

export PYENV_VIRTUALENV_DISABLE_PROMPT=1
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

export PATH="$HOME/.local/bin:$PATH"

set -u
