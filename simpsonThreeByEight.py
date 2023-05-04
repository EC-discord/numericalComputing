import decimal
import math

decimal.getcontext().prec = 8

n = 2
a = 4
b = 10

h = (b - a) / n
h = decimal.Decimal(h)

def fOfX(x):
    x=decimal.Decimal(x)
    # return x*decimal.Decimal(math.exp(x))
    return 1/(1+decimal.Decimal(x**2))

x = []
y = []

for i in range(a, b + 1, int(h)):
    x.append(i)
    y.append(fOfX(i).quantize(decimal.Decimal("0.0001")))

print(x)
print(y)

s = 0
for i in range(1, len(y)-1):
    if i % 3 == 0:
        continue
    s += y[i]

print("Answer: " + str(((3*h)/8)*((y[0] + y[len(y)-1])+3*(s)+2*(sum(y[3:len(y)-1:3])))))