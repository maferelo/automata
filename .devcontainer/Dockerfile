ARG IMAGE=mcr.microsoft.com/vscode/devcontainers/python:0-3.8
ARG VARIANT=-bullseye

FROM ${IMAGE}${VARIANT}

ENV \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Allow piped commands to fail at any step
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN \
    apt-get update --allow-releaseinfo-change \
    && apt-get install --no-install-recommends -y curl=7.74.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY scripts/prestart-app.sh /prestart-app.sh
RUN chmod +x /prestart-app.sh

USER vscode

RUN \
    curl https://pyenv.run | bash \
    && curl https://cli-assets.heroku.com/install.sh | sh

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN \
    --mount=type=cache,target=~/.cache/pypoetry \
    curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="$HOME/.local/bin:$PATH" \
    && export PYENV_ROOT="$HOME/.pyenv" \
    && command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH" \
    && eval "$(pyenv init -)" \
    && pyenv virtualenv automata \
    && pyenv global automata \
    && pyenv activate automata \
    && poetry config virtualenvs.create false \
    && poetry install

COPY .pre-commit-config.yaml .

RUN \
    export PYENV_ROOT="$HOME/.pyenv" \
    && command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH" \
    && eval "$(pyenv init -)" \
    && eval "$(pyenv virtualenv-init -)" \
    && git init . \
    && pre-commit install-hooks \
    && pre-commit install

RUN \
    echo "export PYENV_ROOT='$HOME/.pyenv'" >> ~/.bashrc \
    && echo "command -v pyenv >/dev/null || export PATH='$PYENV_ROOT/bin:$PATH'" >> ~/.bashrc \
    && echo "eval '$(pyenv init -)'" >> ~/.bashrc \
    && echo "eval '$(pyenv virtualenv-init -)'" >> ~/.bashrc

COPY . .
