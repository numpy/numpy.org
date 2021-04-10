import re


with open('config.yaml.in', 'r', encoding='utf-8') as templ:
    lines = templ.readlines()

pattern = re.compile('< content\/\w\w\/config.yaml >')
with open('config.yaml', 'w', ) as f:
    for line in lines:
        match = pattern.search(line)
        if match:
            with open(match.group()[2:-2], 'r', encoding='utf-8') as f2:
                for f2_line in f2.readlines():
                    # indent to get correct yaml formatting
                    f.write('    ' + f2_line)
        else:
            f.write(line)
