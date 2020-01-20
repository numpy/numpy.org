#!/bin/sh

set -euo pipefail

# Note: This script file is not called. It is shfited to the deploy.sh
# Refer: https://github.com/numpy/numpy.org/pull/58/files#r336767432

git submodule update --init
hugo

# If it is not present that means build failed.
# docker failure returns non error exit code so travis doesn't come out.
ls ./public