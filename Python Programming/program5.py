
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


number = int(input("Enter a number: "))
factors = find_factors(number)
print(f"The factors of {number} are: {factors}")
