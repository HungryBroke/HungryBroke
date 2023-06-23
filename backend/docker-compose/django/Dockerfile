ARG PYTHON_VERSION=3.10-slim

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Python `build` stage
FROM python as python-build-stage


# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels -r base.txt

# Python `run` stage
FROM python as python-run-stage

ARG APP_HOME=/app
ARG UID
ARG GID

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV UID=${UID:-1000}
ENV GID=${GID:-1000}

WORKDIR ${APP_HOME}

## Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/


# Add custom group and user that use same id as your system,
# so that you can create files in containers without permission errors
RUN addgroup --system --gid ${GID} django && adduser --uid ${UID} --system --ingroup django --home /home/django django && mkdir -p /home/django/.local/bin


# Set HOME environment variable
ENV HOME=/home/django
ENV PATH="/home/django/.local/bin:${PATH}"

# Ensure cache directory and local directory exists for the django user
RUN mkdir -p /home/django/.cache /home/django/.local && chown -R django:django /home/django/.cache /home/django/.local
USER django

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/*

USER root
RUN rm -rf /wheels/

USER django

COPY --chown=django:django --chmod=755 ./docker-compose/django/entrypoint.sh /entrypoint.sh

# copy application code to WORKDIR
COPY --chown=django:django . ${APP_HOME}

# Add local path to path, so we can run things like pytest.
ENV PATH="$PATH:/home/django/.local/bin/"
ENTRYPOINT ["sh", "/entrypoint.sh"]
