def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Undefined (vertical line)'
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope
x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1) separated by space: ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2) separated by space: ").split())

slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
