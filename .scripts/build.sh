#!/bin/sh


# Note: This script file is not called. It is shfited to the deploy.sh
# Refer: https://github.com/numpy/numpy.org/pull/58/files#r336767432

git submodule update --init
hugo

