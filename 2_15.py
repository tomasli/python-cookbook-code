s = '{name} his {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))
print(vars())

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(vars())
print(s.format_map(safesub(vars())))
print('==========================================================')

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(sub('hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
