#!/bin/bash
# Script to cleanup and uninstall
# python package fetched using fetch-numpydeppkg.sh script 
# 

set -ue

cleanup_pkg() {

  pkgname=$1
  workingdir=$2
  setupdir=$3

  if [ -z "$pkgname" ] || [ -z "$workingdir" ] || [ -z "$setupdir" ]; then
    display_help
    exit
  fi

  ygraphviz=`$workingdir/env-${pkgname}/bin/pip3 list | grep graphviz`
  if ! [ -z "$ygraphviz" ];
  then
    $workingdir/env-${pkgname}/bin/pip3 uninstall -y graphviz
  fi

  ypipdeptree=`$workingdir/env-${pkgname}/bin/pip3 list | grep pipdeptree`
  if ! [ -z "$ypipdeptree" ];
  then
    $workingdir/env-${pkgname}/bin/pip3 uninstall -y pipdeptree
  fi

  $workingdir/env-${pkgname}/bin/pip3 uninstall -y -r $workingdir/numpy_${pkgname}_dep/$setupdir/requirements.txt

  \rm -rf $workingdir/env-${pkgname}
  \rm -rf $workingdir/numpy_${pkgname}_dep

  return 0
}

display_help() {
  echo "-----------------------------------------------------------------------"
  echo "Usage:"
  echo ""
  echo "./cleanup-numpydeppkg.sh pkgname workingdir setupdirname"
  echo ""
  echo "where:"
  echo ""
  echo "pkgname - the name of package in pypi directory"
  echo "workingdir - the directory where latest sources are located"
  echo "setupdirname - the name of top level source directory that contains
  setup.py for the package."
  echo ""
  echo "For example, to download ehtim use the following command:"
  echo ""
  echo "./cleanup-numpydeppkg.sh <pkgname> <working-dir> <setupdirname>"
  echo ""
  echo "-----------------------------------------------------------------------"
}

if [[ ( $# -gt 3) || ( -z "$1" )|| ( -z "$2" ) || ( -z "$3" ) || ("$1" == "-h" ) || ("$1" == "--help") ]];
then
  display_help
  exit
fi

cleanup_pkg $1 $2 $3

echo Done!
