import os
import re


with open('config.yaml.in', 'r', encoding='utf-8') as templ:
    lines = templ.readlines()

pattern = re.compile('< content\/\w\w\/\w*.yaml >')
with open('config.yaml', 'w', encoding='utf-8') as f:
    for line in lines:
        match = pattern.search(line)
        if match:
            with open(match.group()[2:-2], 'r', encoding='utf-8') as f2:
                for f2_line in f2.readlines():
                    # indent to get correct yaml formatting
                    f.write('    ' + f2_line)
        elif line.startswith('disableLanguages'):
            if os.environ.get('NUMPYORG_WITH_TRANSLATIONS'):
                line = "#" + line

            f.write(line)
        else:
            f.write(line)
