import math

def _solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = (real_part + imaginary_part * 1j)
        root2 = (real_part - imaginary_part * 1j)
        return (root1, root2)

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

solutions = _solve_quadratic_eqn(a, b, c)
print(f"The solutions to the quadratic equation are: {solutions}")
