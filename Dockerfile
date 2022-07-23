ARG IMAGE=tiangolo/uvicorn-gunicorn-fastapi:python3.8
ARG STAGING_VARIANT=
ARG VARIANT=-slim


FROM ${IMAGE}${STAGING_VARIANT} as stage

WORKDIR /tmp

ENV DEBIAN_FRONTEND=noninteractive

# Allow piped commands to fail at any step
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM ${IMAGE}${VARIANT}

COPY scripts/prestart.sh /prestart.sh
RUN chmod +x /prestart.sh

RUN addgroup --system app && adduser --system --group app

USER app

WORKDIR /app

COPY --from=stage /tmp/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

ENV PATH="${PATH}:/home/app/.local/bin" \
    PYTHONPATH="${PYTHONPATH}:/home/app/.local/lib/python3.8/site-packages" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=

COPY . .

ENTRYPOINT gunicorn app.main:app -k uvicorn.workers.UvicornWorker --worker-tmp-dir /dev/shm -b 0.0.0.0:${PORT:-5000}
