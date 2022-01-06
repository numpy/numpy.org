# type `make help` to see all options
.DEFAULT_GOAL := help

BASEURL ?= 

ifdef BASEURL
	BASEURLARG=-b $(BASEURL)
endif 

.PHONY: help prepare teams-clean teams serve clean

prepare:
	git submodule update --init --recursive
	python gen_config.py

serve: ## serve the website at http://localhost:1313/
serve: prepare
	hugo $(BASEURLARG) --i18n-warnings server -D

html: ## build the static website in ./public
html: prepare
	hugo $(BASEURLARG)

clean: ## remove build artifacts
	rm -rf public

TEAMS_DIR = static/gallery
TEAMS = emeritus-maintainers maintainers triage-team survey-team web-team
TEAMS_QUERY = python themes/scientific-python-hugo-theme/tools/team_query.py

$(TEAMS_DIR):
	mkdir -p $(TEAMS_DIR)

$(TEAMS_DIR)/%.md: $(TEAMS_DIR)
	$(TEAMS_QUERY) --org numpy --team "$*"  >  $(TEAMS_DIR)/$*.html

teams-clean: prepare
	for team in $(TEAMS); do \
	  rm -f $(TEAMS_DIR)/$${team}.html ;\
	done

teams: ## generate numpy.org team gallery pages
teams: | teams-clean $(patsubst %,$(TEAMS_DIR)/%.md,$(TEAMS))

help:   ## display this message
	@echo numpy.org make targets
	@echo ----------------------
	@python scripts/makefile_to_help.py Makefile
