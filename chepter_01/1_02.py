def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)

print('\n')

records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
        ]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        print('+================')
        print(*args)
        print(args)
        print(type(args))
        do_foo(*args)
    elif tag == 'bar':
        print('-================')
        print(*args)
        print(args)
        print(type(args))
        do_bar(*args)

print('\n')

line = 'nobody:*:-2:-2:UnprivilegedUser:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(*fields)
print(fields)
print(homedir)
print(sh)

print('\n')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

print('\n')

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
