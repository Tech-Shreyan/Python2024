def is_sparse_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    total_elements = rows * columns
    zero_count = sum(row.count(0) for row in matrix)
    if zero_count > total_elements / 2:
        return True
    else:
        return False
def main():
    try:
        rows = int(input("Enter the number of rows in the matrix: "))
        columns = int(input("Enter the number of columns in the matrix: "))
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
    if is_sparse_matrix(matrix):
        print("The given matrix is a sparse matrix.")
    else:
        print("The given matrix is not a sparse matrix.")
if __name__ == "__main__":
    main()
