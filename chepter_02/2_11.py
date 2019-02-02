s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----------hello=============='
print(t.lstrip('-'))
print(t.rstrip('='))
print('=================')


s = '    hello    world     \n'
print(s.strip())
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))
