#!/usr/bin/env bash

set -x

cd /src/linkely &&
    poetry install --no-dev &&
    poetry run ./manage.py migrate &&
    poetry run ./manage.py collectstatic --no-input &&
    poetry run ./manage.py runserver 0.0.0.0:8000
