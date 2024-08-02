
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def generate_prime_series(n):
    prime_series = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_series.append(i)
    return prime_series


n = int(input("Enter a number: "))


prime_series = generate_prime_series(n)
print(f"The prime numbers up to {n} are: {prime_series}")
