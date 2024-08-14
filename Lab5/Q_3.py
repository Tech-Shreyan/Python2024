fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1:n//2 + 1]
else:
    middle_items = food_stuff_lt[n//2]
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
del food_stuff_tp
print(f"Combined food_stuff_tp tuple: {food_stuff_lt}")
print(f"Middle item(s): {middle_items}")
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")
