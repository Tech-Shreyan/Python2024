
def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    while n > 0:
        fibonacci_series.append(a)
        a, b = b, a + b
        n -= 1
    return fibonacci_series
n = int(input("Enter the number of terms: "))


fibonacci_series = generate_fibonacci(n)

print(f"Fibonacci series up to {n} terms:")
print(fibonacci_series)
