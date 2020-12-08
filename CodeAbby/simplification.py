import re
user = re.compile("^.*?Username\s*?=\s*?([\w/]+).*$")
with open('file_for_names.txt') as f:
    [print (name) for name in sorted({user.match(i).group(1) for i in f if user.match(i)})]