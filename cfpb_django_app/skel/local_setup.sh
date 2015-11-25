#!/bin/sh

# Setup script for local development
# NOTE: Run this script while in the back-end root directory.

# Set script to exit on any errors.
set -e

# Install back-end dependencies.
install(){
  echo 'Installing back-end dependencies...'
  pip install -r requirements/testing.txt
  # npm install
  # grunt build

}

# Setup local data store in sqlite
dbsetup(){
  source .env
  echo 'Setting up local sqlite database'
  python manage.py syncdb --noinput --no-initial-data
  python manage.py migrate 
  # python manage.py loaddata somedata.json
  # python manage.py rebuild_index
}

install
dbsetup
