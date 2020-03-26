#!/usr/bin/env python3

"""
This script builds the Team Page Gallery for NumPy.
It is inspired from the code in pandas/pandas-web project.
It can be used to build team page for any project that supports
GitHub https://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts

It requires as input a team.yml configuration file.
You can refer to a sample in ./team/numpy folder.

This configuration file should contain:
```
team:
	template_path: <path_to_the_jinja2_templates_directory>
	base_template: <template_file_all_other_files_will_extend>
	ignore:
	- <list_of_files_in_the_source_that_will_not_be_copied_or_processed>
	github_repo_url: <organization/repo-name>
	context_preprocessors:
	- <list_of_functions_that_will_enrich_the_context_parsed_in_this_file>
	markdown_extensions:
	- <list_of_markdown_extensions_that_will_be_loaded>
	maintainers:
		core: <list_of_core_dev_team_members_github_handle>
		webteam: <list_of_numpy_webteam_members_github_handle>
		documentation: <list_of_numpy_documentation_team_members>
		emeritus: <list_of_emeritus_team_numpy>
```
The rest of the items in the file will be added directly to the context.

Run ./team.py --help to see how to run it.

Example:

	* To run the script use:
		./team.py <Dir Path to yml file location> --ignore-io-errors

	This will pull information about team members listed in yaml file into a local file called team.context. In subsequent runs, unless the team changes, you can reuse this locally stored information to render it using this script and play with layout, css etc. as shown in the next example.


	* To run the script using github info stored locally, use: 
		./team.py <Dir Path to yml file location> --ignore-io-errors --stored-context="team.context"
"""

import os
import sys
import importlib
import typing
import markdown
import shutil
import time
import jinja2
import requests
import yaml
import argparse

class Preprocessors:
	"""
	Built-in context preprocessors.

	Context preprocessors are functions that receive the context used to
    render the templates, and enriches it with additional information.

	The original context is obtained by parsing ``team.yml`` and
	anything else needed just be added with context preprocessors.

	There could be additional context preprocessors such as navbars, blogs
	for NumPy we only have team context pre-processing for now.  Others may be
	added later in this script.
    """

	@staticmethod
	def team_add_info(context):
		"""
		Given the maintainers defined in the yaml file, it fetches
        the GitHub user information for them.
        """

		stored_ctx_fname = context["stored_context"]
		if ( stored_ctx_fname != "" ):
			with open(stored_ctx_fname) as f:
				storedctx = yaml.safe_load(f)
			return storedctx

		context["main"]["maintainers"]["people"] = []
		for user in context["main"]["maintainers"]["core"]:
			resp = requests.get(f"https://api.github.com/users/{user}")
			if context["ignore_io_errors"] and resp.status_code == 403:
				print("Failed to get data for user.....",user)
				return context
			resp.raise_for_status()
			context["main"]["maintainers"]["people"].append(resp.json())

		context["main"]["maintainers"]["webpeople"] = []
		for user in context["main"]["maintainers"]["webteam"]:
			resp = requests.get(f"https://api.github.com/users/{user}")
			if context["ignore_io_errors"] and resp.status_code == 403:
				print("Failed to get data for user.....",user)
				return context
			resp.raise_for_status()
			context["main"]["maintainers"]["webpeople"].append(resp.json())

		context["main"]["maintainers"]["docpeople"] = []
		for user in context["main"]["maintainers"]["documentation"]:
			resp = requests.get(f"https://api.github.com/users/{user}")
			if context["ignore_io_errors"] and resp.status_code == 403:
				print("Failed to get data for user.....",user)
				return context
			resp.raise_for_status()
			context["main"]["maintainers"]["docpeople"].append(resp.json())

		context["main"]["maintainers"]["emerpeople"] = []
		for user in context["main"]["maintainers"]["emeritus"]:
			resp = requests.get(f"https://api.github.com/users/{user}")
			if context["ignore_io_errors"] and resp.status_code == 403:
				print("Failed to get data for user.....",user)
				return context
			resp.raise_for_status()
			context["main"]["maintainers"]["emerpeople"].append(resp.json())

		local_file = os.path.join(os.getcwd(), "team.context")
		print("Storing github info in local file =", local_file)
		with open(local_file, "w") as st_f:
			yaml.dump(context, st_f)

		return context

def get_callable(obj_as_str: str) -> object:
	"""
	Get a Python object from its string representation.
	"""
	components = obj_as_str.split(".")
	attrs = []
	name = __file__.strip('.py')
	name = name.strip('/')

	while components:
		try:
			#obj = importlib.import_module(".".join(components))
			obj = importlib.import_module(name)
		except ImportError:
			attrs.insert(0, components(pop))
		else:
			break
	if not obj:
		raise ImportError(f'Could not import "{obj_as_str}"')

	for attr in attrs:
		obj = getattr(obj, attr)

	obj = getattr(obj, "Preprocessors")
	obj = getattr(obj,"team_add_info")

	return obj

def get_context(contrib_fname: str, ignore_io_errors: bool, **kwargs):
	"""
	Load contrib yaml as base context and add information by context preprocessor for team
	"""
	with open(contrib_fname) as f:
		context = yaml.safe_load(f)

	context["ignore_io_errors"] = ignore_io_errors
	context.update(kwargs)

	preprocessors = (
			get_callable(context_prep)
			for context_prep in context["main"]["context_preprocessors"]
	)

	for preprocessor in preprocessors:
		context = preprocessor(context)
		msg = f"{preprocessor.__name__} is missing the return statement"
		assert context is not None, msg

	return context

def get_source_files(source_path: str) -> typing.Generator[str, None, None]:
	for root, dirs, fnames in os.walk(source_path):
		root = os.path.relpath(root, source_path)
		for fname in fnames:
			yield os.path.join(root, fname)

def extend_base_template(content: str, base_template: str) -> str:
	result = '{% extends "' + base_template + '" %}'
	result += '{% block body %}'
	result += content
	result += '{% endblock %}'
	return result

def main(source_path: str,
		 target_path: str,
		 stored_context: str,
		 ignore_io_errors: bool) -> int:
	"""
	Copy all files in source dir to the target dir

	For ``.md`` and ``.html`` files, render them with context
	before copying them. ``.md`` files are transformed to HTML.
	"""

	contrib_fname = os.path.join(source_path, "team.yml")
	shutil.rmtree(target_path, ignore_errors=True)
	os.makedirs(target_path, exist_ok=True)
	sys.stderr.write("Generating context...\n")
	context = get_context(contrib_fname, ignore_io_errors, stored_context=stored_context)
	sys.stderr.write("Context generated successfully. \n")
	templates_path = os.path.join(source_path,
								  context["main"]["templates_path"])
	jinja_env = jinja2.Environment(
					loader=jinja2.FileSystemLoader(templates_path))

	for fname in get_source_files(source_path):
		if fname in context["main"]["ignore"]:
			continue

		sys.stderr.write(f"Processing {fname}\n")
		dirname = os.path.dirname(fname)
		os.makedirs(os.path.join(target_path, dirname), exist_ok=True)

		extension = os.path.splitext(fname)[-1]
		if extension in (".html", ".md"):
				with open(os.path.join(source_path, fname)) as f:
					content = f.read()
				if extension == ".md":
					body = markdown.markdown(
									content,
									extensions=context["main"]["markdown_extensions"]
					)
					content = extend_base_template(
									body,
									context["main"]["base_template"])
				content = (jinja_env.from_string(content).render(**context))

				fname = os.path.splitext(fname)[0] + ".html"
				with open(os.path.join(target_path,fname), 'w') as f:
					f.write(content)
		else:
				shutil.copy(os.path.join(source_path, fname),
								os.path.join(target_path, dirname))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Team Page builder.")
	parser.add_argument("source_path",
                        help="path to the source directory "
                             "(must contain team.yml)")
	parser.add_argument("--target-path", default="build",
                        help="directory where to write the output")
	parser.add_argument("--stored-context", default="",
						help="Use stored context locally instead of web request to github for data. Default is to seek data from github and store it locally in a file named team.context that can be used in subsequenct runs.")
	parser.add_argument("--ignore-io-errors", action="store_true",
                        help="do not fail if errors happen when fetching "
                             "data from http sources, and those fail "
                             "(mostly useful to allow github quota errors "
                             "when running the script locally)")
	args = parser.parse_args()
	sys.exit(main(args.source_path,
				  args.target_path,
				  args.stored_context,
				  args.ignore_io_errors))
