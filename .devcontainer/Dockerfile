ARG IMAGE=mcr.microsoft.com/vscode/devcontainers/python:0-3.8
ARG VARIANT=-bullseye


FROM ${IMAGE}${VARIANT}

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER vscode

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && curl https://cli-assets.heroku.com/install.sh | sh

ENV PATH "/home/vscode/.poetry/bin:$PATH"

COPY ./pyproject.toml ./poetry.lock* /app/

RUN --mount=type=cache,target=~/.cache/pypoetry \
    poetry config virtualenvs.create false && poetry install 

COPY . .