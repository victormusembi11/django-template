#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Set default values for admin user
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"johndoe42@example.com"}
SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"johndoe"}

cd /app/

mkdir -p /app/static
python manage.py collectstatic --noinput
>&2 echo 'Collected static files...'

/opt/venv/bin/python manage.py migrate --noinput || true
>&2 echo 'Ran database migrations...'

/opt/venv/bin/python manage.py createsuperuser --username $SUPERUSER_USERNAME --email $SUPERUSER_EMAIL --noinput || true
>&2 echo 'Created superuser...'

APP_PORT=${PORT:-8000}

>&2 echo 'About to run Gunicorn...'
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm config.wsgi:application --bind "0.0.0.0:${APP_PORT}" --timeout 600 
