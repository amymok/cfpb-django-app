#!/bin/sh

# Set script to exit on any errors.
set -e

# Initialize front-end dependency directories.
init(){
  NODE_DIR=node_modules
  BOWER_DIR=bower_components

  if [ -f .bowerrc ]; then
    # Get the "directory" line from .bowerrc
    BOWER_DIR=$(grep "directory" .bowerrc | cut -d '"' -f 4)
  fi

  echo 'npm components directory:' $NODE_DIR
  echo 'Bower components directory:' $BOWER_DIR
}

# Clean front-end dependencies.
clean(){
  # If the node and bower directories already exist,
  # clear them so we know we're working with a clean
  # slate of the dependencies listed in package.json
  # and bower.json.
  if [ -d $NODE_DIR ] || [ -d $BOWER_DIR ]; then
    echo 'Removing front-end dependency directories...'
    rm -rf $NODE_DIR
    rm -rf $BOWER_DIR
  fi
  echo 'Front-end dependencies have been removed.'
}

# Install front-end dependencies.
install(){
  echo 'Installing front-end dependencies...'
  npm install
  bower install --config.interactive=false
}

# Run tasks to build the front-end for distribution.
build(){
  echo 'Building front-end...'
  gulp clean
  gulp build
}

init
clean
install
build
