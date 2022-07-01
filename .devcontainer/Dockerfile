ARG IMAGE_SOURCE=python
ARG PYTHON_VERSION=3.8.13
ARG VARIANT=-buster
FROM ${IMAGE_SOURCE}:${PYTHON_VERSION}${VARIANT} as requirements-stage

WORKDIR /app

# Install Poetry
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y curl ca-certificates && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install 

# copy project
COPY . .