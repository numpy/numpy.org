#!/bin/bash
# Script to trim eht-imaging project (M87 blackhole study) dependency graph in dot format
# Trimming is done such that only NumPy oriented dependencies are in focus
# For more details on eht-imaging project visit:
# https://github.com/achael/eht-imaging
# https://achael.github.io/_pages/imaging/

display_help() {

  echo "Usage:"
  echo " numpy-ehtim-dep-graph.sh reqfilepath outputdir [optional color]"
  echo ""
  echo "reqfilepath - directory containing latest source of eht-imaging requirements.txt file."
  echo "outputdir - dir or path where generated graphs will be stored."
  echo "optional color. For e.g., cyan, crimson or any of the https://graphviz.gitlab.io/_pages/doc/info/colors.html specifications for graphviz. Default cyan."
  echo ""
}

check_pre_requisites() {
  yehtim=`pip list | grep ehtim`
  ygraphviz=`pip list | grep graphviz`
  ypipdeptree=`pip list | grep pipdeptree`
  if [[ ( -z "$yehtim" ) || ( -z "$ygraphviz" ) || ( -z "$ypipdeptree" ) ]];
  then
    echo "Error: Pre-requisite for generating dependency graph not fulfilled!"
    echo "The following packages must be installed:"
    echo " 1. ehtim"
    echo " 2. graphviz"
    echo " 3. pipdeptree"
    exit 
  fi
}

if [[ ($# -lt 2) || ($# -gt 3 ) || ( -z "$1" ) || (-z "$2") || ("$1" == "-h") || ("$1" == "--help") ]];
then
  display_help
  exit
fi

reqfilepath=$1
reqfile="$1/requirements.txt"
if ! [ -f $reqfile ];
then
  echo "Error: Make sure you have latest eht-imaging sources and requirements.txt file path is correct!!"
  display_help
  exit 
fi

graphdir="$2"
if [[ ( ! -d "$graphdir" ) || ( -f "$graphdir" ) ]];
then
  echo "Error: Make sure $graphdir is a valid directory to store generated graphs!"
  display_help
  exit 
fi

check_pre_requisites
echo "Using $reqfile to prune dependency graph of ehtim."
echo "Specified output directory is $graphdir."
echo "Generating ehtim dependency graphs..."

pipdeptree --graph-output dot > $graphdir/numpy-ehtim-dep.dot
dot -T png $graphdir/numpy-ehtim-dep.dot -o $graphdir/numpy-ehtim-dep.png

awk '/^[0-9]*[.]+/ {printf(" %s\n", $0); found=1; next} !/^[0-9]*[.]+/ {printf((found==1)? "%s" : "\n%s", $0); found=0 } END {print ""}' $graphdir/numpy-ehtim-dep.dot > $graphdir/cleanup.dot
echo digraph { > $graphdir/cleanup_pkg.dot

awk ' NR==FNR{a[$1]; next} {for (i in a) if ((index($0, i)&& $3 == "") || ($3 != "" && index($0, i) && index($3, i) )) print}' $reqfile $graphdir/cleanup.dot >> $graphdir/cleanup_pkg.dot

echo } >> $graphdir/cleanup_pkg.dot

dot -K twopi $graphdir/cleanup_pkg.dot -o $graphdir/numpy-clean.dot
dot -T png $graphdir/numpy-clean.dot -o $graphdir/numpy-clean.png

if [ -z "$3" ];
then
  #hcolor="crimson"
  hcolor="cyan"
else
  hcolor="$3"
fi

echo "Highlighting numpy nodes using $hcolor." 

awk -v ac=${hcolor} '{ if ($1 == "numpy") {print $0, "color=",ac,", style=filled," } else { if ($2 == "->" && $3 == "numpy") {print $0, "color=",ac,","} else {print}}}' $graphdir/numpy-clean.dot > $graphdir/numpy-clean-color.dot

dot -T png $graphdir/numpy-clean-color.dot -o $graphdir/numpy-clean-color.png

echo "-------------------------------------------------------------------"
echo Done!
