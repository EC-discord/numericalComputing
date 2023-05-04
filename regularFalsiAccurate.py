import decimal
import math
decimal.getcontext().prec = 10
# decimal.getcontext().traps[decimal.FloatOperation] = True
x0 = x1 = "null"
x2 = 0
def function(x):
    x = decimal.Decimal(x).quantize(decimal.Decimal('0.0001'))
    return (x**3 - 2 * x - 5).quantize(decimal.Decimal('0.0001'))

intervalTable = "x | f(x)"

for i in range(0, 10, 1):
    intervalTable += f"\n{i} | {function(i)}"
    if (function(i) * function(i+1)) < 0:
        intervalTable += f"\n{i+1} | {function(i+1)}"
        x0 = i
        x1 = i + 1
        break
if x0 == "null" or x1 == "null":
    print("Could not find the interval")
    exit()
print(intervalTable)
print("Interval")
print(f"[{x0}, {x1}]")
for i in range(20):
    x2 = decimal.Decimal(x0) - function(decimal.Decimal(x0)).quantize(decimal.Decimal('0.0001')) * (((decimal.Decimal(x1) - decimal.Decimal(x0)) / (function(decimal.Decimal(x1)).quantize(decimal.Decimal('0.0001')) - function(decimal.Decimal(x0).quantize(decimal.Decimal('0.0001'))))).quantize(decimal.Decimal('0.0001')))
    print(f"x{i+2}: {x2.quantize(decimal.Decimal('0.0001'))}")
    print(f"f(x{i+2}) = f({x2}) = {function(decimal.Decimal(x2).quantize(decimal.Decimal('0.0001')))}")
    if function(decimal.Decimal(x2).quantize(decimal.Decimal('0.0001'))) > 0:
        x1 = x2
    elif function(decimal.Decimal(x2).quantize(decimal.Decimal('0.0001'))) < 0:
        x0 = x2
