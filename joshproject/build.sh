#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# This script does 3 important things:

# Installs all required Python packages.
# Collects all static files (HTML, CSS, JS).
# Applies any database migrations.