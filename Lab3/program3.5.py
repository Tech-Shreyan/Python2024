def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

example_list = [1, 2, 3, 4, 5]
reversed_example_list = reverse_list(example_list)
print(f"Original list: {example_list}")
print(f"Reversed list: {reversed_example_list}")
