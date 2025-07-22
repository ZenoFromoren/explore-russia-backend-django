#!/bin/bash

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

python explore_russia_backend_django/manage.py flush --no-input
python explore_russia_backend_django/manage.py migrate

exec "$@"