ARG SOURCE=python
ARG VERSION=3.8.13
ARG VARIANT=-buster
FROM ${SOURCE}:${VERSION}${VARIANT} as requirements-stage

WORKDIR /app

# Install Poetry and Heroku CLI
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y curl ca-certificates && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false && \
    curl https://cli-assets.heroku.com/install.sh | sh

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install 

# copy project
COPY . .