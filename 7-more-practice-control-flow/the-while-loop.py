"""
This script demonstrates the use of while loops in Python

1. The first two while loop examples (commented out) increment a counter and print its value until it exceeds 5
2. The last while loop prompts the user to input a number greater than 10
    - If the input is valid, it thanks the user and exits the loop
    - Otherwise, it asks the user to try again
"""

# count = 0

# while count <= 5:
#     print(count)
#     count += 1
    
# print(count)

# count = 0

# while count <= 5:
#     print(count)
#     count +=1

invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print(f"Thanks, that works! {user_value} is a great choice!")
        break
    else:
        print("That doesnt fit! Try again!")