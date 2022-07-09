ARG SOURCE=tiangolo/uvicorn-gunicorn-fastapi
ARG VERSION=python3.8
ARG STAGING_VARIANT=
ARG VARIANT=-slim
FROM ${SOURCE}:${VERSION}${STAGING_VARIANT} as requirements-stage

WORKDIR /tmp

# Install Poetry
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y curl ca-certificates && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM ${SOURCE}:${VERSION}${VARIANT}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# copy project
COPY . .