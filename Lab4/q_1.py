def find_range(arr):
    if not arr:  
        return None  
    min_value = min(arr)
    max_value = max(arr)
    range_value = max_value - min_value
    return range_value
def main():
    input_array = input("Enter a 1D array of numbers separated by spaces: ")
    try:
        arr = list(map(float, input_array.split()))
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return
    range_value = find_range(arr)
    if range_value is not None:
        print(f"The range of the array is: {range_value}")
    else:
        print("The array is empty, so the range cannot be calculated.")
if __name__ == "__main__":
    main()
