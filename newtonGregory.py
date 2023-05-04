import decimal
import math

decimal.getcontext().prec = 6

xToFind = 52

x = [45, 50, 55, 60]
y = [[decimal.Decimal(0.7071), decimal.Decimal(0.7660), decimal.Decimal(0.8192), decimal.Decimal(0.8660)]]

x = [decimal.Decimal(i) for i in x]
y = [[decimal.Decimal(i).quantize(decimal.Decimal('0.0001')) for i in y[0]]]
xToFind = decimal.Decimal(xToFind)

for i in range(len(y[0]) - 1):
    y.append([])

for i in range(len(y[0]) - 1):
    for j in range(len(y[0]) - i - 1):
        y[i+1].append(y[i][j+1] - y[i][j])

print(y)

h = decimal.Decimal(x[1] - x[0])
fOfX = y[0][0]

print(f"f({str(xToFind)}) = {fOfX}", end=" ")

for i in range(len(y[0]) - 1):
    u = (xToFind - x[0]) / h
    un = u
    for j in range(i):
        un *= u - j - 1
    un = decimal.Decimal(un)
    yo = y[i+1][0]
    nextIter = (decimal.Decimal(1/math.factorial(i+1)) * un * yo).quantize(decimal.Decimal('0.0001'))
    fOfX += nextIter
    if nextIter:
        print(f"+ {nextIter}", end=" ")
    else:
        print(f" {nextIter}", end=" ")
print()
print(f"f({str(xToFind)}) = {fOfX}")