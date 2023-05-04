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
    return 1/(1+x**2)

x = []
y = []

for i in range(a, b + 1, int(h)):
    x.append(i)
    y.append(fOfX(i).quantize(decimal.Decimal("0.0001")))

print(x)
print(y)

print(f"(h/3)*(({y[0]} + {y[len(y)-1]})+4*({' + '.join([str(i) for i in y[1:len(y)-1:2]])})+2*({' + '.join([str(i) for i in y[2:len(y)-1:2]])})))")
print("Answer: " + str((h/3)*((y[0] + y[len(y)-1])+4*(sum(y[1:len(y)-1:2]))+2*(sum(y[2:len(y)-1:2])))))