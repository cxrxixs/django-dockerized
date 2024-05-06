#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn core.wsgi --bind 0.0.0.0:8000 --timeout 60 --access-logfile - --error-logfile -
