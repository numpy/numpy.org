#!/bin/sh

# Should be moved to build.sh
# NOTE: Running build.sh and then deploy.sh is not finding the public
# folder which is generated after the build command (hugo).
git submodule update --init
hugo

# deploy in surge
npm install -g surge

if [ -z "$REF" ]
then
      echo "\$REF is not present. Use the PR_NUMBER: $PR_NUMBER ."
      if [ "$PR_NUMBER" == "false" ]
      then
        echo "PR_NUMBER value is ${PR_NUMBER}. Expecting integer number."
        exit 3
      fi
else
  if [ "$PR_NUMBER" != "false" ]
  then
      echo "\$REF is NOT empty. Getting the PR number from the REF variable."
      echo "REF value is ${REF}"
      PR_NUMBER="$(echo $REF | cut -d'/' -f3)"
  else
    echo "PR_NUMBER value is ${PR_NUMBER}."
  fi
fi

PROJECT_BUILD="./public"
DOMAIN="http://numpy-${PR_NUMBER}.surge.sh"
echo "PR_NUMBER: $PR_NUMBER"
echo "SURGE_LOGIN: $SURGE_LOGIN"
echo "SURGE_TOKEN: $SURGE_TOKEN"
ls "./public"

surge --project $PROJECT_BUILD --domain $DOMAIN;

echo ::set-output name=deployed-domain::"pr-${PR_NUMBER}-numpy.org.surge.sh"
