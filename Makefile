# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =

ALLSPHINXOPTS   = -d _build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html upload

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  upload USER=...  to upload to numpy.scipy.org"
	@echo "  html      to make standalone HTML files"

clean:
	-rm -rf _build/*

upload: html
	chmod ug=rwX,o=rX -R _build/html
	rsync -r -z --delete-after -p \
	    _build/html/ \
	    $(USER)@new.scipy.org:/srv/www/numpy/

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

