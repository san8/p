#! /bin/bash

echo "running development server daemon"
nohup python manage.py runserver 127.0.0.1:8000  &

echo "running celery workers daemon"
sh ./bin/celery_multi.sh

