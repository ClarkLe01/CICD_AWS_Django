#!/bin/bash

set -o errexit
set -o nounset

python manage.py migrate
gunicorn -b 0.0.0.0:8000 settings.wsgi