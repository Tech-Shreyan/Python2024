def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)
base = 2
exponent = 3
result = power_recursive(base, exponent)

print(f"{base} to the power of {exponent} is: {result}")
