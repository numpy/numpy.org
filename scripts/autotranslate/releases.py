"""Automatic translation of list of releases.

To add a new language:

First add a function that translates an English datestring of the form "%d %b
%Y" to the corresponding string in the target language to the dictionary
``translate_date_funcs``, keyed by the associated two letter language code.

Second, add a translation for the English phrase "release notes" to the
``release_notes`` dictionary, keyed by the associated two letter language
code.

At build time, the releases.md file at

    ``"scripts/autotranslate/data/releases.md"``

will be translated and translations will be added to

    ``"generated/releases/xx/releases.md"``

for language codes xx corresponding to languages for which translations will
be published.
"""


import functools
import os
import re
import yaml

from datetime import datetime
from pathlib import Path

from autotranslate_common import get_languages, translate_file


month_names_pt = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", 
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]


def translate_date_en_ja(date_string: str) -> str:
    date_object = datetime.strptime(date_string, "%d %b %Y")
    output = date_object.strftime("%Y年%m月%d日")
    # Remove zero padding if needed before return
    return output.replace("年0", "年").replace("月0", "月")


def translate_date_en_pt(date_string: str) -> str:
    date_object = datetime.strptime(date_string, "%d %b %Y")
    return (
        f"{date_object.day} de {month_names_pt[date_object.month - 1]}"
        f" de {date_object.year}"
    )


translate_date_funcs = {
    "pt": translate_date_en_pt,
    "ja": translate_date_en_ja,
}


def translate_date(date_string, language_code):
    return translate_date_funcs[language_code](date_string)


release_notes = {
    "pt": "notas de versão",
    "ja": "リリースノート",
}


def _translate_release_line(release_line: str, language_code: str) -> str:
    """Translate a single line from releases file."""
    if language_code not in release_notes:
        # Fall back to no translation if language is unsupported.
        return release_line
    pattern = (
        r"- NumPy (?P<version>\d+\.\d+\.\d+) "
        r"\(\[release notes\]\((?P<url>.+)\)\) "
        r"-- _(?P<date>.+)_\."
    )
    match = re.search(pattern, release_line)
    if not match:
        raise ValueError(f"Invalid input for release_line, {release_line}")
    version = match.group("version")
    url = match.group("url")
    date = match.group("date")
    return (
        f"- NumPy {version} ([{release_notes[language_code]}]({url})) --"
        f" _{translate_date(date, language_code)}_."
    )


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    toplevel_dir = current_dir.parent.parent
    releases_path = current_dir / "data" / "releases.md"
    for language_code in get_languages():
        destination_dir = toplevel_dir / "generated" / "releases" / language_code
        os.makedirs(destination_dir, exist_ok=True)
        outpath = destination_dir / "releases.md"
        translate_func = functools.partial(
            _translate_release_line, language_code=language_code
        )
        translate_file(releases_path, outpath, translate_func)
