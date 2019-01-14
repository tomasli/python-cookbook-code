line = 'asdf fjdk; afed, fjek,asdf,     foo'
import re
print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s', line)
print(fields)
