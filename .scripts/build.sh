#!/bin/sh

set -euo pipefail

# Note: This script file is not called. It is shfited to the deploy.sh
# Refer: https://github.com/numpy/numpy.org/pull/58/files#r336767432

git submodule update --init
hugo

echo $?

if [ $? -eq 0 ]
then
  echo "Success: build."
  exit 0
else
  echo "Failure: Error while building" >&2
  exit 1
fi