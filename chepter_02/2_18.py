text = 'foo = 23 + 42 * 10'

import re
NAME = r'(?P<Name>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print(master_pat)

scanner = master_pat.scanner('foo = 42')
print(scanner.match())
# not work
print(_.lastgroup,_group())

