#!/bin/bash

cd linkely &&
    ./manage.py migrate &&
    ./manage.py runserver 0.0.0.0:8000
