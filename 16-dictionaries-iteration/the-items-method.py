college_course = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein"
}

for course, professor in college_course.items():
    print(f"The course {course} is being taught by {professor}")
    
# for _, professor in college_course.items():
#     professor("The next professor is {professor}")