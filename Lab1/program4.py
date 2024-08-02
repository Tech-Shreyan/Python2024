
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = reversed_num * 10 + remainder
        n = n // 10
    return reversed_num

number = int(input("Enter a number: "))
reversed_num = reverse_number(number)
print(f"The reverse of the number {number} is {reversed_num}")
