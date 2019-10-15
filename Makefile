.PHONY: serve html clean github

serve:
	@hugo --i18n-warnings server -D

html:
	@hugo
	@touch public/.nojekyll

clean:
	@rm -rf public

github: | clean html
	@echo "Command to upload to git goes here"
	@echo "See `push_dir_to_repo.py` in NumPy"
