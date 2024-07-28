def sum_of_digits(num):
   
    digits = str(num)
    

    sum_digits = sum(int(digit) for digit in digits)
    
    return sum_digits

number = int(input("Enter a number: "))


sum_digits = sum_of_digits(number)


print(f"The sum of the digits of {number} is: {sum_digits}")
