#!/bin/sh

set -euo pipefail

# Should be moved to build.sh
# NOTE: Running build.sh and then deploy.sh is not finding the public
# folder which is generated after the build command (hugo).
git submodule update --init
hugo

# deploy in surge
npm install -g surge

if [ "$PR_NUMBER" != "false" ]
then
    echo "PR_NUMBER value is ${PR_NUMBER}"
else
  echo "PR_NUMBER value is ${PR_NUMBER}."
  exit 3
fi

PROJECT_BUILD="./public"
DOMAIN="http://numpy-${PR_NUMBER}.surge.sh"
echo "PR_NUMBER: $PR_NUMBER"
echo "SURGE_LOGIN: $SURGE_LOGIN"
echo "SURGE_TOKEN: $SURGE_TOKEN"
ls "./public"

surge --project $PROJECT_BUILD --domain $DOMAIN;

echo ::set-output name=deployed-domain::"numpy-${PR_NUMBER}.surge.sh"
