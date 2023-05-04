import decimal
import math
decimal.getcontext().prec = 5
# decimal.getcontext().traps[decimal.FloatOperation] = True
a = b = "null"
x = 0
def function(x):
    x = decimal.Decimal(x)
    return x * decimal.Decimal(math.log(x)) - decimal.Decimal(2.3026)

intervalTable = "x | f(x)"

for i in range(1, 10, 1):
    intervalTable += f"\n{i} | {function(i)}"
    if (function(i) * function(i+1)) < 0:
        intervalTable += f"\n{i+1} | {function(i+1)}"
        a = i
        b = i + 1
        break
if a == "null" or b == "null":
    print("Could not find the interval")
    exit()
print(intervalTable)
print("Interval")
print(f"[{a}, {b}]")
for i in range(20):
    x = decimal.Decimal((a + b) / 2)
    print(f"x{i}: {x}")
    print(f"f(x{i}) = f({x}) = {function(x)}")
    if function(x) > 0:
        b = x
    elif function(x) < 0:
        a = x