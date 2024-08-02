
def swap(a, b):
    return b, a
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
x, y = swap(x, y)
print(f"The first number after swapping: {x}")
print(f"The second number after swapping: {y}")
