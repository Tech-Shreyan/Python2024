def sum_of_diagonal_elements(matrix):
    n = len(matrix) 
    sum_diagonal = 0
    for i in range(n):
        sum_diagonal += matrix[i][i]   
    return sum_diagonal
def main():
    n = int(input("Enter the size of the 2D array (n for an n x n matrix): "))
    matrix = []
    print("Enter the elements row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Invalid row length. Please enter exactly", n, "integers.")
            return
        matrix.append(row)
    sum_diagonal = sum_of_diagonal_elements(matrix)
    print(f"The sum of diagonal elements in the matrix is: {sum_diagonal}")
if __name__ == "__main__":
    main()
