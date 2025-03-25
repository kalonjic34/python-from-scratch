# Flow Control in Python: What I Learned

This document provides a detailed summary of the key concepts and lessons I learned while exploring flow control in Python programming. Flow control is essential for making decisions, repeating tasks, and creating interactive programs. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Conditional Statements
File: [blocks.py](2-flow-control-in-programming/blocks.py)

Conditional statements (`if`, `elif`, `else`) allow programs to make decisions based on specific conditions. I learned how to structure these statements to handle different scenarios, including nested conditions and special cases. For example, checking if a user is old enough to vote or handling unique cases like a specific input value.

```python
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
```

---

## 2. Logical Operators
File: [conditions.py](2-flow-control-in-programming/conditions.py)

Logical operators such as `and`, `or`, and `not` are used to combine multiple conditions. I also learned how to use Python's `in` keyword and `range()` function to simplify conditions. These operators are crucial for writing concise and readable code when dealing with complex decision-making scenarios.

```python
age = int(input("How old are you? "))

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")
```

---

## 3. Loops: `while` and `for`
### While Loops
File: [whileloops.py](2-flow-control-in-programming/whileloops.py)

`While` loops are used to repeat a block of code as long as a condition is true. I learned how to use them for tasks where the number of iterations is not predetermined, such as waiting for user input or processing data until a condition is met.

```python
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
```

### For Loops
File: [forloops.py](2-flow-control-in-programming/forloops.py)

`For` loops are ideal for iterating over sequences like strings, lists, or ranges. I explored how to use them to process each element in a sequence, such as printing each character in a string.

```python
parrot = "Norwegian Blue"

for character in parrot:
    print(character)
```

---

## 4. Nested Loops
File: [timetable.py](2-flow-control-in-programming/timetable.py)

Nested loops allow for operations on multiple levels, such as generating a multiplication table. I learned how to use loops within loops to handle more complex tasks that require iterating over multiple dimensions of data.

```python
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} * {1} is {2}".format(j, i, i * j))
    print("------------------")
```

---

## 5. Breaking and Continuing Loops
File: [shopping.py](2-flow-control-in-programming/shopping.py)

The `break` statement is used to exit a loop prematurely when a specific condition is met, while the `continue` statement skips the rest of the current iteration and moves to the next one. These tools are essential for controlling the flow of loops and handling special cases efficiently.

```python
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)
```

---

## 6. Searching in Lists
File: [searching.py](2-flow-control-in-programming/searching.py)

I learned how to search for items in a list using the `in` keyword and the `.index()` method. This is a fundamental skill for working with collections of data, allowing programs to locate and process specific elements efficiently.

```python
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
```

---

## 7. Input Validation and Conditions
File: [truefalse.py](2-flow-control-in-programming/truefalse.py)

Validating user input is a critical part of creating robust programs. I explored how to check if input is empty or meets specific criteria, ensuring that the program behaves correctly even when given unexpected input.

```python
name = input("Please enter your name: ")

if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
```

---

## 8. Range and Step in Loops
File: [ranges.py](2-flow-control-in-programming/ranges.py)

The `range()` function is a powerful tool for generating sequences of numbers. I learned how to use it with step values to control the increments or decrements in loops, making it easier to iterate over specific ranges of values.

```python
for i in range(10, 0, -2):
    print("i is now {}".format(i))
```

---

## 9. Guessing Games
### Number Guessing Game
File: [guessinggame.py](2-flow-control-in-programming/guessinggame.py)

I implemented a simple guessing game where the user tries to guess a randomly generated number. This exercise reinforced the use of `while` loops, conditions, and user input handling to create an interactive program.

```python
import random

highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
```

---

## 10. Input Parsing and Summation
File: [strings2.py](2-flow-control-in-programming/strings2.py)

I learned how to parse user input to extract numeric values and calculate their sum. This involved identifying separators, splitting the input into individual numbers, and converting them to integers.

```python
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of flow control in Python, including:
- Making decisions with conditional statements (`if`, `elif`, `else`).
- Repeating tasks with loops (`for`, `while`) and controlling them with `break` and `continue`.
- Validating and processing user input to ensure program robustness.
- Searching, parsing, and analyzing data in lists and strings.
- Creating interactive programs like games and utilities.

These skills are essential for writing dynamic and interactive Python programs, and they form the foundation for tackling more advanced programming challenges.
