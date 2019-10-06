#!/bin/sh

npm install -g surge

echo "REF value is ${REF}"

PR_NUMBER="$(echo $REF | cut -d'/' -f3)"
echo "PR_NUMBER: $PR_NUMBER"


surge --project "./public" --domain "pr-${PR_NUMBER}-numpy.org-newsite.surge.sh";

echo ::set-output name=deployed-domain::"pr-${PR_NUMBER}-numpy.org-newsite.surge.sh"
