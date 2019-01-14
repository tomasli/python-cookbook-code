line = 'asdf fjdk; afed, fjek,asdf,     foo'
import re
print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
