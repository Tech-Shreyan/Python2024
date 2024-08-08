def sum_of_odd_numbers(matrix):
    sum_odd = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:
                sum_odd += num
    return sum_odd
def main():
    try:
        rows = int(input("Enter the number of rows in the 2D array: "))
        columns = int(input("Enter the number of columns in the 2D array: "))
        if rows <= 0 or columns <= 0:
            print("The number of rows and columns should be positive integers.")
            return
    except ValueError:
        print("Invalid input. Please enter valid integers for rows and columns.")
        return
    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(rows):
        try:
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            if len(row) != columns:
                print(f"Invalid input. Please enter exactly {columns} integers for row {i + 1}.")
                return
            matrix.append(row)
        except ValueError:
            print("Invalid input. Please enter valid integers for the matrix elements.")
            return
    sum_odd = sum_of_odd_numbers(matrix)
    print(f"The sum of all odd numbers in the matrix is: {sum_odd}")
if __name__ == "__main__":
    main()
