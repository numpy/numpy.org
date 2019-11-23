#!/bin/sh

# Should be moved to build.sh
# NOTE: Running build.sh and then deploy.sh is not finding the public
# folder which is generated after the build command (hugo).
git submodule update --init

# Find PR number and determine where to deploy to with GitHub Actions
PR_NUMBER="$(echo $REF | cut -d'/' -f3)"
DOMAIN_NOHTTP="numpy-${PR_NUMBER}.surge.sh"
DOMAIN="http://numpy-${PR_NUMBER}.surge.sh"

# Adapt baseURL to Surge deploy URL, otherwise links generated by Hugo
# won't work.
sed -i -e 's/numpy.org/'"$DOMAIN_NOHTTP"'/g' config.yaml

# Generate site
hugo

# deploy in Surge
npm install -g surge

echo "REF value is ${REF}"

PROJECT_BUILD="./public"
echo "PR_NUMBER: $PR_NUMBER"
echo "SURGE_LOGIN: $SURGE_LOGIN"
echo "SURGE_TOKEN: $SURGE_TOKEN"
ls "./public"

surge --project $PROJECT_BUILD --domain $DOMAIN;

echo ::set-output name=deployed-domain::$DOMAIN
