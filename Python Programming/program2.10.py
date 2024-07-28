import math

def is_krishnamurthy_number(num):
    digits = str(num)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    
    return sum_of_factorials == num


number = int(input("Enter a number: "))

if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
