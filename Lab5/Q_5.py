A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_union_B = A.union(B)
A_intersection_B = A.intersection(B)
is_A_subset_of_B = A.issubset(B)
are_A_and_B_disjoint = A.isdisjoint(B)
A_joined_with_B = A.union(B)
B_joined_with_A = B.union(A)
symmetric_difference_A_B = A.symmetric_difference(B)
del A
del B
print(f"Union of A and B: {A_union_B}")
print(f"Intersection of A and B: {A_intersection_B}")
print(f"Is A a subset of B? {is_A_subset_of_B}")
print(f"Are A and B disjoint sets? {are_A_and_B_disjoint}")
print(f"Join A with B: {A_joined_with_B}")
print(f"Join B with A: {B_joined_with_A}")
print(f"Symmetric difference between A and B: {symmetric_difference_A_B}")
try:
    print(A)
    print(B)
except NameError:
    print("Sets A and B have been deleted and no longer exist.")

