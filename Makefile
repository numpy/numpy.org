# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =

ALLSPHINXOPTS   = -d _build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html upload

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  upload     to upload to numpy.github.com"
	@echo "  html       to make standalone HTML files"
	@echo "  linkcheck  to check if external links work"
	@echo "  clean      to remove build directory"

clean:
	-rm -rf _build/*

upload: html
	cd _build/html && \
	    touch .nojekyll && \
	    echo numpy.scipy.org > CNAME && \
	    rm -rf .git && \
	    git init && \
	    git remote add target git@github.com:numpy/numpy.github.com.git && \
	    git add -A && \
	    git commit -m "Rebuild site" -a && \
	    git push -f target master:master

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) _build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
              "or in _build/linkcheck/output.txt."

