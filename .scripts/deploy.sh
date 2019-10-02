#!/bin/bash

npm install -g surge

DEPLOY_DOMAIN = pr-$1-numpy.org-newsite.surge.sh
DEPLOY_PATH = "./public"
echo ${github.actor}
echo $DEPLOY_DOMAIN
echo $PR

surge --project ${DEPLOY_PATH} --domain $DEPLOY_DOMAIN;
