def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
def main():
    input_array = input("Enter an array of integers separated by spaces: ")
    try:
        arr = list(map(int, input_array.split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    reverse_array(arr)
    print("Reversed array:", arr)
if __name__ == "__main__":
    main()
