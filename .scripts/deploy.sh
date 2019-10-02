#!/bin/bash

npm install -g surge

echo "${REF} REF value is "
echo ${REF}
echo "$REF"

echo "$PR_NUMBER"
echo "${PR_NUMBER}"
echo "$array[2]"
echo "${array[2]}"

surge --project "./public" --domain "pr-${PR_NUMBER}-numpy.org-newsite.surge.sh";

echo ::set-output name=deployed-domain::"pr-${PR_NUMBER}-numpy.org-newsite.surge.sh"
