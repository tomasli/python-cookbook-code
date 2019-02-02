data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
print('\n')

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
print('\n')

data = b'FOO:BAR,SPAM'
import re
print(re.split(b'[:,]', data))
print('\n')

a = 'Hello World'
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])
print(b.decode('ascii'))

