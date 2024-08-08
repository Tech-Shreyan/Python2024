def sum_of_even_numbers(arr):
    sum_even = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
    return sum_even
def main():
    input_array = input("Enter an integer array separated by spaces: ")
    try:
        arr = list(map(int, input_array.split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    sum_even = sum_of_even_numbers(arr)
    print(f"The sum of even numbers in the array is: {sum_even}")
if __name__ == "__main__":
    main()
