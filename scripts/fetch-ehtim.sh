#!/bin/bash
# Script to fetch and install eht-imaging project (M87 blackhole study)
# For more details on eht-imaging refer to the links below:
# https://github.com/achael/eht-imaging
# https://achael.github.io/_pages/imaging/

# The following function does the following:
# 1. Fetches latest eht-imaging software in specified working dir
#    (default current-dir/numpy_ehtim_dep)
# 2. Assumes virtualenv, python and pip are available and installs graphviz, pipdeptree
# 3. Git clones eht-imaging package
#
# To generate eht-imaging package dependency graph and highlight the role of NumPy
# use the script numpy-ehtim-dep-graph.sh
# 

get_latest_ehtim() {

  nowdir=`pwd`
  cd $1
  
  if [ -d numpy_ehtim_dep ];
  then
    \rm -rf numpy_ehtim_dep
  fi
  mkdir numpy_ehtim_dep 
  cd numpy_ehtim_dep
  
  virtualenv EHTIMENV
  source EHTIMENV/bin/activate

  ygraphviz=`pip list | grep graphviz`
  if [ -z "$ygraphviz" ];
  then
    pip install graphviz
  fi

  ypipdeptree=`pip list | grep pipdeptree`
  if [ -z "$ypipdeptree" ];
  then
    pip install pipdeptree
  fi
  
  git clone https://github.com/achael/eht-imaging.git
  cd eht-imaging
  pip install .

  deactivate 
  cd $nowdir
  return 0
}

display_help() {
  echo "Usage:"
  echo ""
  echo "./fetch-ehtim.sh workingdir"
  echo ""
  echo "where workingdir is the directory where latest eht-imaging sources will be git cloned and built."
  echo ""
}

curdir=`pwd`

if [[ ( $# -gt 1 ) || ( -z "$1" ) || ("$1" == "-h" ) || ("$1" == "--help") ]];
then
  display_help
  exit
fi

if [ ! -d "$1" ];
then
  echo "Error: $1 is not a valid directory!!!"
  exit
fi

get_latest_ehtim $1

echo Done!
