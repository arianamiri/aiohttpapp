#!/bin/bash

# GET ABSOLUTE PATHS TO SOURCE DIRECTORY
# location of this script
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# source code top level directory
BASEDIR="$(dirname "$BASEDIR")"

# build the dev db image
DEV_DB_IMAGE_DIR="$BASEDIR/images/dev_db/"
docker build -t local/dev_db $DEV_DB_IMAGE_DIR

# build the web app container
cd $BASEDIR
docker build -t bakeoff .

# VOLUMES DIRECTORY
# Things like db data need to be persisted when 
# the containers and shut down and restarted.
VOLUMES_DIR="$BASEDIR/volumes/db/"

if [ ! -d $VOLUMES_DIR ]; then
    mkdir -p $VOLUMES_DIR
fi
