s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, don;t lok around the eyes, look into my eyes, you're under"

import textwrap

print(textwrap.fill(s, 70))
print('\n')
print(textwrap.fill(s, 40))
print('\n')
print(textwrap.fill(s, 40, initial_indent=' '))
print('\n')
print(textwrap.fill(s, 40, subsequent_indent=' '))
