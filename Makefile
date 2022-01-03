# type `make help` to see all options 

# If you have naively forked this repo, say to
# github.com://myname/numpy.org.git, you can test out the build via
# make TARGET=myname BASEURL=https://myname.github.io/numpy.org deploy

TARGET ?= origin
BASEURL ?= 

ifdef BASEURL
	BASEURLARG=-b $(BASEURL)
endif 

all: build

.PHONY: serve html clean deploy help prepare

.SILENT: # remove this to see the commands executed

prepare:
	git submodule update --init --recursive
	python gen_config.py

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

teams: | teams-clean $(patsubst %,$(TEAMS_DIR)/%.md,$(TEAMS))

public: ## create a worktree branch in the public directory
	git worktree add -B gh-pages public $(TARGET)/gh-pages
	rm -rf public/*

serve: prepare ## serve the website
	hugo --i18n-warnings server -D

html: prepare public ## build the website in ./public
	hugo $(BASEURLARG)
	touch public/.nojekyll

public/.nojekyll: html

clean: ## remove the build artifacts, mainly the "public" directory
	rm -rf public
	git worktree prune
	rm -rf .git/worktrees/public

deploy: public/.nojekyll ## push the built site to the gh-pages of this repo
	cd public && git add --all && git commit -m"Publishing to gh-pages"
	@echo pushint to $(TARGET) gh-pages
	git push $(TARGET) gh-pages

hugo: ## for local development
	python gen_config.py
	hugo $(BASEURLARG)

# Add help text after each target name starting with '\#\#'
help:   ## Show this help.
	@echo "\nHelp for this makefile"
	@echo "Possible commands are:"
	@grep -h "##" $(MAKEFILE_LIST) | grep -v grep | sed -e 's/\(.*\):.*##\(.*\)/    \1: \2/'
	@echo 
	@echo If you have naively forked this repo, say to
	@echo github.com://myname/numpy.org.git, you can test out the build via
	@echo make TARGET=myname BASEURL=https://myname.github.io/numpy.org deploy
