ARG IMAGE=mcr.microsoft.com/vscode/devcontainers/python:0-3.8
ARG VARIANT=-bullseye


FROM ${IMAGE}${VARIANT}

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl ca-certificates \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && curl https://cli-assets.heroku.com/install.sh | sh

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install 

COPY . .