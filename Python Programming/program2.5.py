import math


sin_60 = math.sin(math.radians(60))


cos_pi = math.cos(math.pi)


sin_value = math.sin(0.8660254037844386)

try:
    tan_90 = math.tan(math.radians(90))
except ValueError as e:
    tan_90 = str(e)

print(f"Sin of 60 degrees is: {sin_60}")
print(f"Cos of pi is: {cos_pi}")
print(f"Sin(0.8660254037844386) is: {sin_value}")
print(f"Tan of 90 degrees is: {tan_90}")
