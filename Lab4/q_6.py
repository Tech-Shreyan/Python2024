def find_smallest_number(arr):
    if len(arr) == 0:
        return None  
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    smallest_number = find_smallest_number(arr)
    if smallest_number is not None:
        print(f"The smallest number in the array is: {smallest_number}")
    else:
        print("The array is empty.")
if __name__ == "__main__":
    main()
