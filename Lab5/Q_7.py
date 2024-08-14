student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}
length_of_student_dict = len(student)
skills = student['skills']
skills_data_type = type(skills)
student['skills'].extend(['Machine Learning', 'Web Development'])
keys_list = list(student.keys())
values_list = list(student.values())
student_items = list(student.items())
del student['address']
del student
print(f"Length of student dictionary: {length_of_student_dict}")
print(f"Skills: {skills}")
print(f"Data type of skills: {skills_data_type}")
print(f"Modified skills: {skills}")
print(f"Keys in student dictionary: {keys_list}")
print(f"Values in student dictionary: {values_list}")
print(f"Student dictionary as list of tuples: {student_items}")
try:
    print(student)
except NameError:
    print("The student dictionary has been deleted and no longer exists.")
