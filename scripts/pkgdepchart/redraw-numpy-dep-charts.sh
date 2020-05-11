#!/bin/bash
# This script refreshes all numpy dependency graphs for packages
# that are mentioned in NumPy case studes: ehtim, gwpy and PyCBC
#

set -ue

scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

curdir=`pwd`
outputdir=$curdir

if [[ "$#" -ge "2" || (( "$#" -eq "1" ) && ( "$1" == "-h" || "$1" == "--help" )) ]]; then
    echo ""
    echo "Usage:  ./redraw-numpy-dep-charts.sh outputdirname <optional, default current-dir"
    echo ""
    exit
fi

if [[ $# -eq "0" ]]; then
    echo "Warning: No output dir specified, using $curdir as default output dir." 
elif [[ $# -eq "1" ]]; then
        outputdir=$1
fi
    
if ! [[ -d $outputdir ]]; then
    echo "Warning: Specified output directory: $outputdir does not exist!!!"
    exit
fi

# Using /tmp/numpy and the package source processing dir for dependency graphs

workingdir="/tmp/numpy"
if [ -d $workingdir ];
then
    \rm -rf $workingdir
fi
mkdir $workingdir

declare -a pkgarray=("ehtim" "gwpy" "PyCBC")
declare -a pkgurl=("https://github.com/achael/eht-imaging.git"
                   "https://github.com/gwpy/gwpy.git"
                   "https://github.com/gwastro/pycbc.git")
declare -a pkgsetup=("eht-imaging" "gwpy" "pycbc")

highlightcolor="cyan"

#numpkg=${#pkgarray[@]}

for index in "${!pkgarray[@]}" ; 
do
    echo ".....Drawing ${pkgarray[$index]} dependency chart....."
    echo "Using....pkgurl = ${pkgurl[$index]}"
    echo "installing pkg from dir pkgsetup = ${pkgsetup[$index]}"
    echo "and using $workingdir as scratch"

    mkdir $workingdir/${pkgarray[$index]} $workingdir/${pkgarray[$index]}/graphdir
    ${scriptdir}/fetch-numpydeppkg.sh ${pkgarray[$index]} $workingdir/${pkgarray[$index]} ${pkgurl[$index]} ${pkgsetup[$index]}
    ${scriptdir}/gen-numpy-dep-graph.sh ${pkgarray[$index]} $workingdir/${pkgarray[$index]} $workingdir/${pkgarray[$index]}/numpy_${pkgarray[$index]}_dep/${pkgsetup[$index]} $workingdir/${pkgarray[$index]}/graphdir/ $highlightcolor
    if ! [ -f $workingdir/${pkgarray[$index]}/graphdir/numpy-clean-color.png ]
    then
        echo "Error: Graph for ${pkgarray[$index]} failed! Exiting."
        exit
    fi
    cp $workingdir/${pkgarray[$index]}/graphdir/numpy-clean-color.png $outputdir/${pkgarray[$index]}-numpy-dep-graph.png
done

#Clean up
for index in "${!pkgarray[@]}" ;
do
    echo "Uninstalling ${pkgarray[$index]}....."
    ${scriptdir}/cleanup-numpydeppkg.sh ${pkgarray[$index]} $workingdir/${pkgarray[$index]} ${pkgsetup[$index]}
done

echo "Cleaning up scratch dir: $workingdir..........."
\rm -rf $workingdir
echo "Done!"
