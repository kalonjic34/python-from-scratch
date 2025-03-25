# ### 1. **Event Eligibility**
# Write a program that asks the user for their name and age. 
# If their age is between 21 and 40 (inclusive), print a message saying they are eligible to attend a special event. 
# Otherwise, print a message saying they are not eligible.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 21 and age <= 40:
    print("Hi,{}. You are eligible to attend a special event".format(name))
else:
    print("Sorry {}, you are not eligible".format())

# ### 2. **Favorite Activity Filter**
# Create a program that asks the user what their favorite activity is. 
# If the activity does not include the word "reading" (case-insensitive), print a message saying, "You should try reading sometime!"

favorite_activity = input("What is your favorite activity ")

if "reading" not in favorite_activity.casefold():
    print("You should try reading sometime!")

# ### 3. **Word Contains Letter**
# Write a program that asks the user to input a sentence and a letter. 
# Check if the letter exists in the sentence. If it does, print how many times the letter appears in the sentence. 
# If it doesn’t, print a message saying the letter is not in the sentence.

write_sentence = input("Input a sentence: ")
enter_letter = input("Input a letter: ")

if enter_letter in write_sentence:
    count = write_sentence.count(enter_letter)
    print("The letter '{}' exist in the sentence: '{}'. letter count: {}".format(enter_letter,write_sentence,count))
else:
    print("The letter '{}' doesnt exist in '{}'".format(enter_letter,write_sentence))

# ### 4. **Number Guessing with Hints**
# Create a guessing game where the user has to guess a number between 1 and 50. 
# After each incorrect guess, provide a hint: "Too high" or "Too low." The user gets five attempts to guess the correct number. 
# If they fail, reveal the correct number.

import random

answer = random.randint(1, 50)
attempts = 5

print("Guess a number between 1 and 50. You have {} attempts.".format(attempts))

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
    attempts -= 1

if attempts == 0:
    print("Sorry, you've run out of attempts. The correct number was {}.".format(answer))
     

# ### 5. **Driving Eligibility**
# Write a program that asks the user for their age. 
# If their age is 16 or older, print "You are eligible to apply for a driver's license." 
# If they are younger than 16, print "You need to wait X more years to apply for a driver's license," 
# where X is the number of years left.

age = int(input("Enter your age: "))

if age >= 16:
    print("You are eligible to apply for a driver's license.")
else:
    years_left = 16 - age
    print("You need to wait {} more year(s) to apply for a driver's license.".format(years_left))