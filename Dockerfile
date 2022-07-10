ARG IMAGE=tiangolo/uvicorn-gunicorn-fastapi:python3.8
ARG STAGING_VARIANT=
ARG VARIANT=-slim


FROM ${SOURCE}${STAGING_VARIANT} as stage

WORKDIR /tmp

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl ca-certificates \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM ${IMAGE}${VARIANT}

WORKDIR /app

RUN useradd --create-home python \
    && chown python:python -R /app

USER python

COPY --from=stage --chown=python:python /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

COPY --chown=python:python . .