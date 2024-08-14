ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
average_age = sum(ages) / len(ages)
age_range = max_age - min_age
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age:.2f}")
print(f"Range of ages: {age_range}")
print(f"Difference between min age and average: {min_diff:.2f}")
print(f"Difference between max age and average: {max_diff:.2f}")
