ARG IMAGE=tiangolo/uvicorn-gunicorn-fastapi:python3.8
ARG STAGING_VARIANT=
ARG VARIANT=-slim


FROM ${IMAGE}${STAGING_VARIANT} as stage

WORKDIR /tmp

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM ${IMAGE}${VARIANT}

RUN addgroup --system app && adduser --system --group app

USER app

COPY --from=stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="${PYTHONPATH}:/home/app/.local/lib/python3.8/site-packages" \
    PATH="${PATH}:/home/app/.local/bin" \
    USER="app"

COPY . .