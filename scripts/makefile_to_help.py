"""
Modified from https://github.com/cesium-ml/baselayer

Convert ## style comments after a Makefile target into help text.

Usage: makefile_to_help.py <MAKEFILE>

"""

import sys
import re


if not sys.argv:
    print("Usage: makefile_to_help.py <MAKEFILE>")
    sys.exit(0)


def describe_targets(lines):
    matches = [re.match('^([\w-]+): +##(.*)', line) for line in lines]
    groups = [m.groups(0) for m in matches if m]
    targets = {target: desc for (target, desc) in groups}

    N = max(len(target) for (target, desc) in targets.items())

    for (target, desc) in targets.items():
        print(f'{target:{N}} {desc}')


fname = sys.argv[1]
describe_targets(open(fname).readlines())
