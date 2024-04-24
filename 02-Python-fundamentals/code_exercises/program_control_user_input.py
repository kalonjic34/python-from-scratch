# TODO: Write a while loop that asks the user if they wish to continue the program
# If the user answers "yes", print "Program is running..." and ask again
# If the user answers "no", print "Program stopped."
# If the user enters any other input, ask again

user_input= input("Do wish to continue the program? (yes/no): ")

while user_input=="yes":
    print("Program is running...")
    user_input= input("Do wish to continue the program? (yes/no): ")
    
print("Program stopped.")