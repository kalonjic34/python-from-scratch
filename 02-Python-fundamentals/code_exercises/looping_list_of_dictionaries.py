# You have a list of student dictionaries containing their names and grades. 
# Write a loop to iterate over the list and print each student's name and grade.

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

# TODO: Write a loop to iterate over the list and print each student's name and grade.

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has {grade}%")