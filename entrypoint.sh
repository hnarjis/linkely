#!/usr/bin/env bash

set -x

pip install -r /src/requirements.txt &&
    /src/linkely/manage.py migrate &&
    /src/linkely/manage.py runserver 0.0.0.0:8000
