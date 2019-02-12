nums = [1,2,3,4,5]
s = sum(x * x for x in nums)
print([x * x for x in nums])
print(s)


import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('sorry, no python.')


s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO','shares':75},
    {'name':'AOL', 'shares':20},
    {'name':'SCOX', 'shares':65}
]
min_share = min(s['shares'] for s in portfolio)
min_share_1 = min(portfolio, key = lambda s: s['shares'])
print(min_share)
print(min_share_1)
