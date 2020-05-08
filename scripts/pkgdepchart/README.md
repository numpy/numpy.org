# NumPy Dependency Chart generator Scripts 

## Overview

Typically, you only need to run the top level script **redraw-numpy-dep-charts.sh.**

Here is how these scripts are organized:

* **Top level script:**  redraw-numpy-dep-charts.sh
* **Helper scripts:** These scripts are used by **redraw-numpy-dep-charts.sh**
and should be run in the suggested order below:

1. fetch-numpydeppkg.sh
2. gen-numpy-dep-graph.sh
3. cleanup-numpydeppkg.sh

If you run the helper scripts, make sure you run them in this order to generate graphs in specified output directory.

Usage details of each script are listed in the section below.

----

## Script: redraw-numpy-dep-charts.sh

### Use Case:

NumPy case studies refers to ehtim, gwpy and PyCBC packages.  For each of these,
we have created NumPy dependency graphs.  You can redraw all these three graphs
in one go (obtain 3 png files) in the specified output directory. If you wish
to add a new package and also refresh existing charts, you can edit the script
and update three arrays:

* *pkgarray:* List of packages for which numpy dependency chart is to be generated
* *pkgurl:* List of github urls from where pkg sources can be git cloned
* *pkgsetup:* Dirname (not path) of the top level dir in pkg source that contains
  requirements.txt file used to pip install the package in a virtualenv.
  The package is uninstalled as part of cleanup after graphs is generated.

#### Usage

redraw-numpy-dep-charts.sh **outputdir**

*outputdir:* The output directory is an optional parameter.

If no output directory is specified, the graphs (.png files) of all the packages
listed in pkgarray variable are generated in the current directory from where 
the script is run.

**Pre-requisites:**

The following software packages must be installed on the system where you are running this bash script:  git, python3, pip3, virtualenv.

----

## Script: fetch-numpydeppkg.sh

### Use Case:

This script is one of the helper scripts used by **redraw-numpy-dep-charts.sh**
script. Its sole purpose is to download the package for which numpy dependency
graph is to be generated and install it in a virtual environment, setup the 
directory structure which can be used by other helper script 
**gen-numpy-dep-graph.sh** to generate the graph.  This script is paired with
**cleanup-numpydeppkg.sh** script for uninstalling and removing scratch data.

#### Usage

fetch-numpydeppkg.sh **package_name scratchdir git_url reqfile_parentdir**

*package_name:*  Name of the package (as in pip registry) that will be fetched.

*scratchdir:* local directory where the package contents will be fetched.

*git_url:*  Full git url required for git cloning.

*reqfile_parentdir:*  This is the name (not path) of the root directory of package that contains requirements.txt file

----

## Script: gen-numpy-dep-graph.sh

### Use Case:

This is a helper script used by **redraw-numpy-dep-charts.sh** script. Its sole
purpose is to use the pre-installed pkg in a local virtual environment by
the script **fetch-numpydeppkg.sh** (or manually installed locally) and use them
to run graphviz, dot and other utilities for creating NumPy dependency chart
as png files for the pkg.  It assumes that packages is pre-installed and does
not clean up any pre-installed packages.  In case a user has the package 
pre-installed and would like to simply generate NumPy dependency chart, this script can be used.

#### Usage:

gen-numpy-dep-graph.sh **package_name scratchdir output_graphdir highlight_color (optional)**

*package_name:* Name of the package (as in pip registry) for which NumPy dependency graph is to be generated.

*scratchdir:* local directory where the package contents reside, the same directory as input to the fetch-numpydeppkg.sh where package_name was fetched by that script.

*output_graphdir:* directory pathname where generated graphs in png format will be stored.

highlight_color:* color understood by dot language.  Default is cyan.  Other
acceptable colors are red, blue.  For a complete list see:

* https://www.graphviz.org/doc/info/lang.html
* https://www.graphviz.org/doc/info/colors.html

**Pre-requisite:**

Please note, **gen-numpy-dep-graph** script needs the virtualenv directory
that was activated and used for package deployment a priori say by
**fetch-numpydeppkg.sh** script or manually by user.  It is assumed that the 
scratchdir comprises of two top level directories - virtualenv dir and another
dir with package_name sources that are git cloned or a local copy of the same.

----

##Script: cleanup-numpydeppkg.sh

### Use Case:

This is a helper script used by **redraw-numpy-dep-charts.sh** script. Its sole
purpose is to cleanup all the packages that were installed by
**fetch-numpydeppkg.sh** script executed prior to running cleanup script. It
 also removes the scratch directory contents related to virtualenv setup and
package sources that were installed by **fetch-numpydeppkg.sh** script. If you
have not used **fetch-numpydeppkg** script then you do not need to run the cleanup script.

#### Usage:

*package_name:*  Name of the package (as in pip registry) that will be uninstalled.

*scratchdir:* local directory where the package contents were earlier fetched by
**fetch-numpydeppkg.sh** script.

*reqfile_parentdir:*  This is the name (not path) of the root directory of
package that contains requirements.txt file. This is needed to uninstall all
package dependencies that were installed as part of fetching and setting up of package by **fetch-numpydeppkg.sh** script.
