def search_element(arr, element):
    if element in arr:
        return arr.index(element)  
    else:
        return -1 
def main():
    input_array = input("Enter a 1D array of numbers separated by spaces: ")
    try:
        arr = list(map(float, input_array.split()))
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return
    try:
        element = float(input("Enter the element to search for: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    index = search_element(arr, element) 
    if index != -1:
        print(f"Element {element} found at index {index}.")
    else:
        print(f"Element {element} not found in the array.")
if __name__ == "__main__":
    main()
