def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == j:
                print('/', end='')
            else:
                print(' ', end='')
        print()

n = int(input("Enter the number of lines (N): "))

print_pattern(n)
