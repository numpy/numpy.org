import os
import re
import yaml


config = yaml.load(
    open("config.yaml.in", "r", encoding="utf-8"), Loader=yaml.SafeLoader
)


def merge_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1:
            if isinstance(value, list):
                d1[key].extend(value)
            elif isinstance(value, dict):
                merge_dicts(d1[key], value)
        else:
            d1[key] = value

    return d1


def include_files(d):
    external = {}
    for key, val in d.items():
        if isinstance(val, dict):
            d[key] = include_files(val)
        elif key == "include-files":
            for otherfile in val:
                external_data = yaml.load(
                    open(otherfile, "r", encoding="utf-8"), Loader=yaml.SafeLoader
                )
                external = merge_dicts(external, external_data)

    d.pop("include-files", None)
    return {**d, **external}


config = include_files(config)
if os.environ.get("NUMPYORG_WITH_TRANSLATIONS"):
    del config["disableLanguages"]


yaml.dump(config, open('config.yaml', 'w', encoding='utf-8'), sort_keys=False)
