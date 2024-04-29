#!/bin/bash
set -e

echo "Running Development Server"
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver 0.0.0.0:8000
