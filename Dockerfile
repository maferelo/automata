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
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-dev

FROM ${IMAGE}${VARIANT}

COPY scripts/postcreate.sh /postcreate.sh
RUN chmod +x /postcreate.sh

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
