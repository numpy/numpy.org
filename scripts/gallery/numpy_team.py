#!/usr/bin/env python3

"""
This script builds the NumPy Team Page Gallery using content/en/team.md file.
The output team.html is stored in static/gallery/ target folder by default.
It is inspired from the code in pandas/pandas-web project.

It requires as input numpy_team.yml configuration file.
This configuration file should contain::

    main:
        template_path: <path_to_the_jinja2_templates_directory>
        base_template: <template_file_all_other_files_will_extend>
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

The rest of the items in the file will be added directly to the context.

Make sure your current directory is gallery which contains numpy_team.py file.

Run ``./numpy_team.py --help`` to see how to run it.

Example:

To run the script use::

    ./numpy_team.py <Dir Path to yml file location>

This will pull information about team members listed in yaml file into a local
file called numpy_team.context. In subsequent runs, unless the team changes,
you can reuse this locally stored information to render it using this script
and play with layout, css etc. as shown in the next example.

To run the script using github info stored locally, use::

    ./numpy_team.py <Dir Path to yml file location> --ignore-io-errors
            --stored-context="cache/numpy_team.context"

"""

import os
import sys
import importlib
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

        info = {'core': 'people', 'webteam': 'webpeople', 'documentation':
                'docpeople', 'emeritus': 'emerpeople'}
        for key, value in info.items():
            context = get_team_gitinfo(key, value, context)

        cache_dir = os.path.join(os.getcwd(), "cache")
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        local_file = os.path.join(cache_dir, "numpy_team.context")
        print("Storing github info in local file =", local_file)
        with open(local_file, "w") as st_f:
            yaml.dump(context, st_f)

        return context


def get_team_gitinfo(subteam, ctx_tag, context):
    """
    Given the subteam kind as input, fetch their info from git.
    """
    context["main"]["maintainers"][ctx_tag] = []
    for user in context["main"]["maintainers"][subteam]:
        resp = requests.get(f"https://api.github.com/users/{user}")
        if context["ignore_io_errors"] and resp.status_code == 403:
            print("Failed to get data for user.....",user)
            return context
        resp.raise_for_status()
        context["main"]["maintainers"][ctx_tag].append(resp.json())

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
    Load contrib yaml as base context and add information by context
    preprocessor for team.
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


def extend_base_template(content: str, base_template: str) -> str:
    result = '{% extends "' + base_template + '" %}'
    result += '{% block body %}'
    result += content
    result += '{% endblock %}'
    return result


def main(config_yaml: str,
         target_path: str,
         stored_context: str,
         ignore_io_errors: bool) -> int:
    """
    Uses Team.md file in Hugo sources content/en subfolder, render it with
    context and transformed it to HTML which is statically included in NumPy
    Hugo static/gallery folder.
    """

    shutil.rmtree(target_path, ignore_errors=True)
    os.makedirs(target_path, exist_ok=True)
    sys.stderr.write("Generating context...\n")
    context = get_context(config_yaml, ignore_io_errors,
                          stored_context=stored_context)
    sys.stderr.write("Context generated successfully. \n")
    templates_path = os.path.join(os.getcwd(),
                                  context["main"]["templates_path"])
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_path))
    fname = "./team.md"
    sys.stderr.write(f"Processing {fname}\n")
    with open(fname, 'r') as f:
        content = f.read()

    body = markdown.markdown(content,
                             extensions=context["main"]["markdown_extensions"])
    content = extend_base_template(body,
                                   context["main"]["base_template"])
    content = (jinja_env.from_string(content).render(**context))
    fname = "team.html"
    with open(os.path.join(target_path,fname), 'w') as f:
        f.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Team Page builder.")
    parser.add_argument("config_yaml",
                        help="directory pathname to the yaml file"
                             "(e.g. ./numpy_team.yml)")
    parser.add_argument("--target-path", default="../../static/gallery",
                        help="directory where to write the output,default ./build")
    parser.add_argument("--stored-context", default="",
                        help="Use stored context locally instead of web request to github for data. Default is to seek data from github and store it locally in a file named team.context that can be used in subsequenct runs.")
    parser.add_argument("--ignore-io-errors", action="store_true",
                        help="do not fail if errors happen when fetching "
                             "data from http sources, and those fail "
                             "(mostly useful to allow github quota errors "
                             "when running the script locally)")
    args = parser.parse_args()
    sys.exit(main(args.config_yaml,
                  args.target_path,
                  args.stored_context,
                  args.ignore_io_errors))
