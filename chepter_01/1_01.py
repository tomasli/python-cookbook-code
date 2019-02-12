p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)

try:
    p = (4, 5)
    x, y, z = p
except Exception as e:
    print('==================================')
    # repr(e) for display Error name
    print(repr(e))
    print('==================================')

s = 'hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)

_, shares, price, _ = data
print(shares)
print(price)
