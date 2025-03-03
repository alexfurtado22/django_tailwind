#!/bin/bash
export GUNICORN_WORKERS=3 
python manage.py collectstatic --no-input
python manage.py migrate
if [[ "$ENV_STATE" == "production" ]]; then
    gunicorn --bind 0.0.0.0:8000 myproject.wsgi --workers ${GUNICORN_WORKERS:-3} --forwarded-allow-ips "*"
else
    python manage.py runserver 0.0.0.0:8000
fi