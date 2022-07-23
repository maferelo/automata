ARG IMAGE=mcr.microsoft.com/vscode/devcontainers/python:0-3.8
ARG VARIANT=-bullseye


FROM ${IMAGE}${VARIANT}

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY scripts/prestart.sh /prestart.sh
RUN chmod +x /prestart.sh

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER vscode

# Allow piped commands to fail at any step
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && curl https://cli-assets.heroku.com/install.sh | sh

ENV PATH "/home/vscode/.poetry/bin:$PATH"

COPY ./pyproject.toml ./poetry.lock* /app/

RUN --mount=type=cache,target=~/.cache/pypoetry \
    poetry config virtualenvs.create false && poetry install

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY . .
