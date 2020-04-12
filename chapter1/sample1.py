
#1.1 Unpacking a Sequence Into Separate Variables


p = (4, 5)
x, y = p

print(x)
print(y)

data = ['ACME', 50, 91.1, (2012,12,21)]

name, shares, prices, date = data

print(name, shares, prices, date)

name, shares, prices, (year, month, day) = data

print(year, month, day)

s = 'Hello'
a, b, c, d, e = s
print ( a, b , c, d, e)

data = ['ACME', 50, 91.1, (2012,12,21)]

_, shares, prices, _ = data

print(shares, prices)