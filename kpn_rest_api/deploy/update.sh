#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/django-kpn-rest-api-demo'

git pull
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py collectstatic --noinput
supervisorctl restart kpn-rest-api

echo "DONE! :)"
