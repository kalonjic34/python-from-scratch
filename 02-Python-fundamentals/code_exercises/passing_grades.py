# You have a list of student dictionaries containing their names and grades. Write a loop to iterate over the list and print only the names of students who have passed (grades greater than or equal to 70).

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 34},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 12},
]

# TODO: Write a loop to iterate over the list and print only the names of students who have passed.
for student in students:
    name = student["name"]
    grade = student["grade"]
    if grade >= 50:
        print(f"{name} has passed with {grade}")