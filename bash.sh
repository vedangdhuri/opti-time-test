#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Convert static files for production
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate
