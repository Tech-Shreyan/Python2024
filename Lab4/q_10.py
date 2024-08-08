def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def count_primes(arr):
    prime_count = 0
    for num in arr:
        if is_prime(num):
            prime_count += 1
    return prime_count
def main():
    input_array = input("Enter an array of integers separated by spaces: ")
    try:
        arr = list(map(int, input_array.split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    prime_count = count_primes(arr)
    print(f"The number of prime numbers in the array is: {prime_count}")
if __name__ == "__main__":
    main()
