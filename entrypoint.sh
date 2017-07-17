#!/usr/bin/env bash

set -x

cd linkely &&
    ./manage.py migrate &&
    ./manage.py runserver 0.0.0.0:8000
