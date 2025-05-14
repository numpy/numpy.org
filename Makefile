# type `make help` to see all options 

BASEURL ?= 

ifdef BASEURL
	BASEURLARG=-b $(BASEURL)
endif 

.PHONY: help prepare teams-clean teams serve clean

# Add help text after each target name starting with '\#\#'
help:   ## show this help
	@echo "\nHelp for this makefile"
	@echo "Possible commands are:"
	@grep -h "##" $(MAKEFILE_LIST) | grep -v grep | sed -e 's/\(.*\):.*##\(.*\)/    \1: \2/'

prepare:
	git submodule update --init
	python gen_config.py

# All translations share the <team>.toml files in the en translation
TEAMS_DIR = content/en/teams
TEAMS = emeritus-maintainers maintainers docs-team triage-team survey-team web-team
TEAMS_QUERY = python themes/scientific-python-hugo-theme/tools/team_query.py

$(TEAMS_DIR)/%.toml:
	$(TEAMS_QUERY) --org numpy --team "$*"  >  $(TEAMS_DIR)/$*.toml

teams-clean: prepare
	for team in $(TEAMS); do \
	  rm -f $(TEAMS_DIR)/$${team}.toml ;\
	done

teams: | teams-clean $(patsubst %,$(TEAMS_DIR)/%.toml,$(TEAMS)) ## generates numpy.org team gallery pages

serve: prepare ## serve the website
	hugo $(BASEURLARG) --printI18nWarnings server -D

# Serve the site for development purposes (leaving submodules as-is, etc).
serve-dev:
	python gen_config.py
	hugo $(BASEURLARG) --printI18nWarnings server --buildDrafts --disableFastRender --poll 1000ms

html: prepare ## build the website in ./public
	hugo $(BASEURLARG)

clean: ## remove the build artifacts, mainly the "public" directory
	rm -rf public

