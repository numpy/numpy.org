#!/bin/sh

# Should be moved to build.sh
# NOTE: Running build.sh and then deploy.sh is not finding the public
# folder which is generated after the build command (hugo).
# git submodule update --init
# hugo

# deploy in surge
npm install -g surge

if [ "$TRAVIS_PULL_REQUEST" != "false" ]
then
    echo "PR_NUMBER value is ${TRAVIS_PULL_REQUEST}"
else
  echo "PR_NUMBER value is ${TRAVIS_PULL_REQUEST}."
  exit 3
fi

PROJECT_BUILD="./public"
DOMAIN="http://numpy-${TRAVIS_PULL_REQUEST}.surge.sh"
echo "SURGE_LOGIN: $SURGE_LOGIN"
echo "SURGE_TOKEN: $SURGE_TOKEN"
ls "./public"

surge --project $PROJECT_BUILD --domain $DOMAIN;

echo "numpy-${TRAVIS_PULL_REQUEST}.surge.sh"
