def display_table(n):
    print("a b a^b a^2 a^3")
    
    for i in range(1, n + 1):
        a = i
        b = 1
        a_b = a ** b
        a_square = a ** 2
        a_cube = a ** 3
        print(f"{a} {b} {a_b} {a_square} {a_cube}")
n = 5
display_table(n)
