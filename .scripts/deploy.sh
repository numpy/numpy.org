#!/bin/sh

npm install -g surge

echo "REF value is ${REF}"

PR_NUMBER="$(echo $REF | cut -d'/' -f3)"
PROJECT_BUILD="./public"
DOMAIN="pr-${PR_NUMBER}-numpy.org-newsite.surge.sh"
echo "PR_NUMBER: $PR_NUMBER"
pwd
ls
ls "./public"

surge --project $PROJECT_BUILD --domain $DOMAIN;

echo ::set-output name=deployed-domain::$DOMAIN
