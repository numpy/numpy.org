#!/bin/bash
# Script to fetch and install python package that depends on numpy
# This script has been tested for eht-imaging, gwpy and pycbc packages
# For more details on eht-imaging refer to the links below:
# https://github.com/achael/eht-imaging
# https://achael.github.io/_pages/imaging/
# For more details on gwpy see: https://github.com/gwpy/gwpy
# For more details on pycbc see: https://github.com/gwastro/pycbc

# The following function does the following:
# 1. Fetches latest software sources for the specified package in the given  working dir
#    (default current-dir/numpy_<pkgname>_dep)
# 2. Assumes python3, virtualenv, python and pip3 are available and installs graphviz, pipdeptree
# 3. Git clones specified package
#
# To generate the dependency graph for the specified package and highlight the
# role of NumPy use the script gen-numpy-dep-graph.sh
# 

get_latest_pkg() {

  pkgname=$1
  nowdir=`pwd`
  workingdir=$2
  cd $workingdir

  if [ -d numpy_${pkgname}_dep ];
  then
    \rm -rf numpy_${pkgname}_dep
  fi
  mkdir numpy_${pkgname}_dep 
  cd numpy_${pkgname}_dep
  
  virtualenv --python=python3 $workingdir/env-${pkgname}
  source $workingdir/env-${pkgname}/bin/activate

  ygraphviz=`$workingdir/env-${pkgname}/bin/pip3 list | grep graphviz`
  if [ -z "$ygraphviz" ];
  then
    $workingdir/env-${pkgname}/bin/pip3 install graphviz
  fi

  ypipdeptree=`$workingdir/env-${pkgname}/bin/pip3 list | grep pipdeptree`
  if [ -z "$ypipdeptree" ];
  then
    $workingdir/env-${pkgname}/bin/pip3 install pipdeptree
  fi
  
  git clone $3 
  cd $4 
  $workingdir/env-${pkgname}/bin/pip3 install .

  deactivate 
  cd $nowdir
  return 0
}

display_help() {
  echo "-----------------------------------------------------------------------"
  echo "Usage:"
  echo ""
  echo "./fetch-numpydeppkg.sh pkgname workingdir github_srcurl setupdirname"
  echo ""
  echo "where:"
  echo ""
  echo "pkgname - the name of package in pypi directory"
  echo "workingdir - the directory where latest sources will be git cloned and
  built"
  echo "github_srcurl - the github link to project sources for git cloning"
  echo "setupdirname - the name of top level source directory that contains"
  echo "setup.py for the package."
  echo ""
  echo "For example, to download ehtim use the following command:"
  echo ""
  echo "./fetch-numpydeppkg.sh pkgname <working-dir>"
  echo "               https://github.com/achael/eht-imaging.git eht-imaging"
  echo ""
  echo "-----------------------------------------------------------------------"
}

curdir=`pwd`

if [[ ( "$#" -gt "4") || ( -z "$1" )|| ( -z "$3" ) || ( -z "$4" ) || ("$1" == "-h" ) || ("$1" == "--help") ]];
then
  display_help
  exit
fi

if [ ! -d "$2" ];
then
  echo "Error: $2 is not a valid directory!!!"
  exit
fi

get_latest_pkg $1 $2 $3 $4

echo Done!
