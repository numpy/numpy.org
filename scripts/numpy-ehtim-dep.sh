#!/bin/bash
# Script to generate eht-imaging project (M87 blackhole study)
# https://github.com/achael/eht-imaging
# https://achael.github.io/_pages/imaging/

# The following function annotates the dependency graph in color highlighting NumPy

highlight_numpy() {
  thisdir=`pwd`
  cd $1
  color=$2
  echo $color is used to highlight NumPy in dependency graph...
  if [ -f graphs/cleanup_twopi.dot ];
  then
    awk -v ac=${color} '{ if ($1 == "numpy") {print $0, "color=",ac,", style=filled," } else { if ($2 == "->" && $3 == "numpy") {print $0, "color=",ac,","} else {print}}}' graphs/cleanup_twopi.dot > graphs/numpy-clean-color.dot
    dot -T png graphs/numpy-clean-color.dot -o graphs/numpy-clean-color.png
  fi
  cd $thisdir
}

# The following function cleans up the default dependency graph
# It fixes lines broken at package version string into single line
# Next, it goes over the latest eht-imaging requirements.txt file and selects
# trims the full dependency chart to correspond to packages listed in that file only

cleanup_dep_graph() {
  savedir=`pwd`
  cd $1
  if [ -d numpy_ehtim_dep ];
  then
    if [ -f $graphdir/numpy-ehtim-dep.dot ];
    then
      awk '/^[0-9]*[.]+/ {printf(" %s\n", $0); found=1; next} !/^[0-9]*[.]+/ {printf((found==1)? "%s" : "\n%s", $0); found=0 } END {print ""}' $graphdir/numpy-ehtim-dep.dot > $graphdir/cleanup.dot
      echo digraph { > graphs/cleanup_pkg.dot
      awk ' NR==FNR{a[$1]; next} {for (i in a) if ((index($0, i)&& $3 == "") || ($3 != "" && index($0, i) && index($3, i) )) print}' numpy_ehtim_dep/eht-imaging/requirements.txt graphs/cleanup.dot >> graphs/cleanup_pkg.dot
      echo } >>graphs/cleanup_pkg.dot
      dot -K twopi graphs/cleanup_pkg.dot -o graphs/cleanup_twopi.dot
      dot -T png graphs/cleanup_twopi.dot -o graphs/numpy-clean.png
    fi 
  fi
  cd $savedir
  return 0
}

# The following function obtains latest eht-imaging software,
# Installs eht-imaging in a virtualenv,
# Creates the full software package dependency graph

get_latest_ehtim() {

  nowdir=`pwd`
  cd $1
  
  if [ -d numpy_ehtim_dep ];
  then
    \rm -rf *
  fi 
  mkdir numpy_ehtim_dep 
    if ! [ -d $graphdir ];
   then
     mkdir $graphdir
   fi
  cd numpy_ehtim_dep
  virtualenv EHTIMENV
  source EHTIMENV/bin/activate
  
  pip install graphviz
  pip install pipdeptree 
  git clone https://github.com/achael/eht-imaging.git
  cd eht-imaging
  pip install .

  cd $graphdir 
  pipdeptree --graph-output dot > numpy-ehtim-dep.dot
  dot -T png numpy-ehtim-dep.dot -o numpy-ehtim-dep.png
 
  deactivate 
  cd $nowdir
  return 0
}

curdir=`pwd`
read -p 'Enter directory name or path for graph output directory (Default: current directory $curdir/numpy_ehtim_dep) ' inputdir

if [ -z "$inputdir" ];
then
   workingdir=$curdir
elif ! [ -d $inputdir ];
then
   echo "You need to specify a valid directory path!!!"
   exit -1
else
   workingdir=$inputdir
fi

graphdir=$workingdir/graphs
echo Obtaining latest ehtim dependency information from sources...
get_latest_ehtim $workingdir
echo Removing secondary and extraneous package information...
cleanup_dep_graph $workingdir
echo Highlighting numpy nodes and arcs in cyan color...
#hcolor="crimson"
hcolor="cyan"
highlight_numpy $workingdir $hcolor
echo Done!
