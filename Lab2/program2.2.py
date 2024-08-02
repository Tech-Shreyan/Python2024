import math

a = 1
b = -3
c = 2


discriminant = b**2 - 4*a*c

if discriminant >= 0:
   
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The solutions are:", root1, "and", root2)
else:
    print("The equation has no real solutions")
