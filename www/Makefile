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
	-rm -rf built_doc

upload: html
	git clone git@github.com:numpy/numpy.github.com built_doc
	cp -r _build/html/* built_doc
	git -C built_doc add -A
	git -C built_doc commit -m "Rebuild site" -a
	git -C built_doc push origin
	rm -rf built_doc

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) _build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
              "or in _build/linkcheck/output.txt."

spelling:
	$(SPHINXBUILD) -b spelling $(ALLSPHINXOPTS) _build/spelling > build.log 2>&1 || { cat build.log; exit 1; }
	@echo
	@cat _build/spelling/output.txt
	@echo
	@test ! -s _build/spelling/output.txt
