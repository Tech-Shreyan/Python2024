def print_digit(digit):
    segments = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|'],
    }
    for line in segments[digit]:
        print(line)

def print_number_as_segment_display(n):
    for digit in str(n):
        print_digit(digit)

n = input("Enter a number: ")
print_number_as_segment_display(n)
