#!/bin/sh
# Script to perform local development
# This script will workon the virtualenv for this project OR, if that
# venv doesn't exist, will create it, initialize front-end and back-end,
# and then be prepared to run.

# Set script to exit on any errors.
set -e

# Setup the back-end development environment
setup_backend(){
    echo 'Creating virtual environment...'
    mkvirtualenv {{app_name}}
    workon {{app_name}}
    echo 'Installing back-end dependencies...'
    pip install -r requirements.txt
    pip install -r requirements_test.txt
    pip install tox
    echo 'Initializing database...'
    python manage.py migrate --noinput --no-initial-data
    # python manage.py loaddata somedata.json
    # python manage.py rebuild_index
}

# Setup the front-end development environment
setup_frontend() {
    echo 'Setting up front-end...'
    sh setup.sh
}

# If the virtualenvironment already exists, we assume everything else is
# setup.
source `which virtualenvwrapper.sh`
{
    workon {{app_name}}
} || {
    setup_backend && setup_frontend
}

