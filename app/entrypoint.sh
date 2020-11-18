#!/bin/sh

if [ "$DATABASE" = "cartloop" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate



celery -A app worker -l info -n default_worker -Q default --autoscale 2,1 -B &
celery -A app worker -l info -n low_worker -Q low_priority -c 1 &
celery -A app worker -l info -n high_worker -Q high_priority --autoscale 4,2 &

python manage.py runserver 0.0.0.0:8000


exec "$@"