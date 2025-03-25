# Question: How can I check if the user's age falls within a specific range (18 to 30 inclusive) 
# and display a personalized message based on whether they meet the criteria?
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18 and age < 31:
    print("Welcome to the 18-30 holidays, {}".format(name)) 
else:
    print("Sorry, {}, you do not meet the age requirements to attend.".format(name))