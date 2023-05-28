#!/usr/bin/env bash

set -x

cd /src/linkely &&
  poetry install --no-dev &&
  poetry run python manage.py migrate &&
  poetry run python manage.py collectstatic --no-input &&
  poetry run gunicorn --bind 0.0.0.0:8000 linkely.wsgi
