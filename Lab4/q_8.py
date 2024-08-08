def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]
    return transposed
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
    transposed_matrix = transpose_matrix(matrix)
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(" ".join(map(str, row)))
if __name__ == "__main__":
    main()
