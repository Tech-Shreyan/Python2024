import math


def factorial_series(n):
    series = []
    for i in range(1, n+1):
        series.append(math.factorial(i))
    return series


num_terms = int(input("Enter the number of terms: "))


series = factorial_series(num_terms)
print(f"The first {num_terms} terms of the series are: {series}")
