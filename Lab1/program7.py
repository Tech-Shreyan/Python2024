
def find_numbers():
    result = []
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            result.append(num)
    return result


numbers = find_numbers()
print("Numbers divisible by 7 but not a multiple of 5, between 1000 and 2000:")
print(numbers)
