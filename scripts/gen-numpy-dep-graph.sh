#!/bin/bash

# gen-numpy-dep-graph.sh script is used to generate numpy dependency
# graph for a given package. If you already don't have the package
# sources available locally, you can use the script get-package
# to download package sources before running this script.
# The full dependency graph is stored as numpy-<pkgname>-dep.png file
# in the specified output directory.  Besides the full chart, for simplicity
# this script trims specified package project dependency graph in dot format
# Trimming is done such that only NumPy oriented dependencies are in focus

# This script along wiht get-package.sh script has been used to create
# NumPy dependency graphs for ehtim-imaging package, gwpy and cbPy packages.
# It should work fine for any specified package that depends on NumPy.
# Feedback is most welcome.

# For more details on eht-imaging project visit: https://github.com/achael/eht-imaging
# For more details on gwpy project visit: https://github.com/gwpy/gwpy

display_help() {
  echo "-----------------------------------------------------------------------"
  echo "Usage:"
  echo " gen-numpy-dep-graph.sh pkgname workingdir reqfilepath outputdir [optional color]"
  echo ""
  echo "pkgname - the name of the package that uses numpy, use the same name
  echo "workingdir - the workingdir pathname where pkgname sources are available"
  that you specify to pip3 to install the package."
  echo "reqfilepath - directory containing latest source of eht-imaging requirements.txt file."
  echo "outputdir - dir or path where generated graphs will be stored."
  echo "optional color. For e.g., cyan, crimson or any of the https://graphviz.gitlab.io/_pages/doc/info/colors.html specifications for graphviz. Default cyan."
  echo ""
  echo "-----------------------------------------------------------------------"
}

check_pre_requisites() {
  pkgname=$1
  vdir="$2/env-$pkgname/bin"
  ypkgname=`$vdir/pip3 list | grep "${pkgname}"`
  ygraphviz=`$vdir/pip3 list | grep graphviz`
  ypipdeptree=`$vdir/pip3 list | grep pipdeptree`
  if [[ ( -z "$ypkgname" ) || ( -z "$ygraphviz" ) || ( -z "$ypipdeptree" ) ]];
  then
    echo "Error: Pre-requisite for generating dependency graph not fulfilled!"
    echo "The following packages must be installed:"
    echo " 1. $pkgname"
    echo " 2. graphviz"
    echo " 3. pipdeptree"
    exit 
  fi
}

if [[ ($# -lt 3) || ($# -gt 5 ) || ( -z "$1" ) || (-z "$2") || (-z "$3") || ("$1" == "-h") || ("$1" == "--help") ]];
then
  display_help
  exit
fi

inputpkgname=$1
venvdir=$2
reqfilepath=$3
reqfile="$3/requirements.txt"
if ! [ -f $reqfile ];
then
  echo "Error: Make sure you have latest $inputpkgname sources and requirements.txt file path is correct!!"
  display_help
  exit 
fi

graphdir="$4"
if [[ ( ! -d "$graphdir" ) || ( -f "$graphdir" ) ]];
then
  echo "Error: Make sure $graphdir is a valid directory to store generated graphs!"
  display_help
  exit 
fi

check_pre_requisites $inputpkgname $venvdir
echo "Using $reqfile to prune dependency graph of $inputpkgname."
echo "Specified output directory is $graphdir."
echo "Generating $inputpkgname dependency graphs..."

inputfile=$graphdir/numpy-${inputpkgname}-dep.dot
outputfile=$graphdir/numpy-${inputpkgname}-dep.png
$venvdir/env-${inputpkgname}/bin/pipdeptree --graph-output dot > $graphdir/numpy-${inputpkgname}-dep.dot
dot -T png $inputfile -o $outputfile

awk '/^[0-9]*[.]+/ {printf(" %s\n", $0); found=1; next} !/^[0-9]*[.]+/ {printf((found==1)? "%s" : "\n%s", $0); found=0 } END {print ""}' $inputfile > $graphdir/cleanup.dot

echo "Cleaning up requirements file...."
reqfiletmp=$graphdir/tmpfile
reqfiletmp1=$graphdir/tmpfile1

sed '/^#/ d' $reqfile > $reqfiletmp
sed '/^$/ d' $reqfiletmp > $reqfiletmp1
awk -F '<|=|>|;' '{print $1}' $reqfiletmp1 > $graphdir/reqfileclean

echo digraph { > $graphdir/cleanup_pkg.dot

awk ' NR==FNR{a[$1]; next} {for (i in a) if ((index($0, i)&& $3 == "") || ($3 != "" && index($0, i) && index($3, i) )) print}' $graphdir/reqfileclean $graphdir/cleanup.dot >> $graphdir/cleanup_pkg.dot

echo "Cleaning up temp files"
\rm -rf $graphdir/tmpfile $graphdir/tmpfile1 $graphdir/reqfileclean
echo } >> $graphdir/cleanup_pkg.dot

dot -K twopi $graphdir/cleanup_pkg.dot -o $graphdir/numpy-clean.dot
dot -T png $graphdir/numpy-clean.dot -o $graphdir/numpy-clean.png

if [ -z "$5" ];
then
  #hcolor="crimson"
  hcolor="cyan"
else
  hcolor="$5"
fi

echo "Highlighting numpy nodes using $hcolor." 

awk -v ac=${hcolor} '{ if ($1 == "numpy") {print $0, "color=",ac,", style=filled," } else { if ($2 == "->" && $3 == "numpy") {print $0, "color=",ac,","} else {print}}}' $graphdir/numpy-clean.dot > $graphdir/numpy-clean-color.dot

dot -T png $graphdir/numpy-clean-color.dot -o $graphdir/numpy-clean-color.png

echo "-------------------------------------------------------------------"
echo Done!
