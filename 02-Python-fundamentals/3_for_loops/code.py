friends = ["James", "Sam", "Ian"]

for friend in friends:
    print(friend)

elements = [0,1,2,3,4,5,6,7,8,9]

for index in elements:
    print("hello")

for index in range(5):
    print(index)

students = [
    {"name" : "James", "grade": 90},
    {"name" : "Sam", "grade": 78},
    {"name" : "Ian", "grade": 100},
    {"name" : "Will", "grade": 80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")