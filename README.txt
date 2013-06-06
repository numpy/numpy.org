This repository contains the Sphinx source for the NumPy website
(http://www.numpy.org/).

After cloning this repository, run

    $ git submodule init
    $ git submodule update

To get the Sphinx theme used.

To make a local build of the website

    $ make html

To build and upload the site (requires push permissions on
https://github.com/numpy/numpy.github.com).

    $ make upload

To test external links from the site

    $ make linkcheck

