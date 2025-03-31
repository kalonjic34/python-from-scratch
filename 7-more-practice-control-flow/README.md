# In-depth: Control Flow

This document provides a detailed summary of the key concepts and lessons I learned while exploring control flow in Python. Control flow allows us to dictate the order in which code is executed, enabling decision-making, looping, and recursion. Below is a breakdown of the topics covered and the insights gained.

---

## 1. The Boolean Data Type, Equality, and Inequality
File: [REVIEW-The-Boolean-data-type-equality-and-inequality.py](7-more-practice-control-flow/REVIEW-The-Boolean-data-type-equality-and-inequality.py)

I learned about the Boolean data type (`True` and `False`) and how to use equality (`==`) and inequality (`!=`) operators to compare values.

```python
handsome = True
admin = False

print(2 < 4)  # Output: True
print("xbox" == "xbox")  # Output: True
print("xbox" != "playstation")  # Output: True
```

---

## 2. The `if` Statement
File: [the-if-statement.py](7-more-practice-control-flow/the-if-statement.py)

The `if` statement allows us to execute code only when a condition is `True`. I explored various examples of conditional checks.

```python
if 5 > 3:
    print("This will be printed because the condition is True.")

if "chris" == "chris":
    print("Great name!")  # Output: Great name!
```

---

## 3. The `else` Statement
File: [the-else-statement.py](7-more-practice-control-flow/the-else-statement.py)

The `else` statement provides an alternative block of code to execute when the `if` condition is `False`.

```python
value = int(input("Enter a number: "))

if value > 1000:
    print("Thinking big!")
else:
    print("That's an okay number.")
```

---

## 4. The `elif` Statement
File: [the-elif-statement.py](7-more-practice-control-flow/the-elif-statement.py)

The `elif` statement allows us to check multiple conditions in sequence. I used it to create a calculator and determine if a number is positive, negative, or zero.

```python
def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Zero"

print(positive_or_negative(5))  # Output: Positive!
```

---

## 5. Conditional Expressions
File: [conditional-expressions.py](7-more-practice-control-flow/conditional-expressions.py)

Conditional expressions (also known as ternary operators) allow us to write concise `if-else` statements.

```python
zip_code = "90210"
check = "Valid" if len(zip_code) == 5 else "Invalid"
print(check)  # Output: Valid
```

---

## 6. The `and` Keyword
File: [the-and-keyword.py](7-more-practice-control-flow/the-and-keyword.py)

The `and` keyword ensures that both conditions must be `True` for the entire expression to evaluate to `True`.

```python
if 5 < 7 and "rain" == "rain":
    print("Both conditions are True.")  # Output: Both conditions are True
```

---

## 7. The `or` Keyword
File: [the-or-keyword.py](7-more-practice-control-flow/the-or-keyword.py)

The `or` keyword ensures that at least one condition must be `True` for the entire expression to evaluate to `True`.

```python
if 5 > 8 or 7 < 11:
    print("At least one condition is True.")  # Output: At least one condition is True
```

---

## 8. The `not` Keyword
File: [the-not-keyword.py](7-more-practice-control-flow/the-not-keyword.py)

The `not` keyword negates a condition, reversing its truth value.

```python
if not 5 > 10:
    print("This will print because the condition is False.")  # Output: This will print
```

---

## 9. Nested `if` Statements
File: [nested-if-statements.py](7-more-practice-control-flow/nested-if-statements.py)

Nested `if` statements allow us to check conditions within other conditions. I used them to provide meal recommendations based on ingredients.

```python
ingredient1 = "Pasta"
ingredient2 = "Meatballs"

if ingredient1 == "Pasta":
    if ingredient2 == "Meatballs":
        print("Make pasta and meatballs.")  # Output: Make pasta and meatballs.
```

---

## 10. The `bool` Function, Truthiness, and Falsiness
File: [the-bool-function-truthiness-and-falsiness.py](7-more-practice-control-flow/the-bool-function-truthiness-and-falsiness.py)

I learned how Python evaluates truthy and falsy values using the `bool` function.

```python
print(bool(1))  # Output: True
print(bool(0))  # Output: False
print(bool(""))  # Output: False
print(bool("Python"))  # Output: True
```

---

## 11. The `while` Loop
File: [the-while-loop.py](7-more-practice-control-flow/the-while-loop.py)

The `while` loop repeatedly executes a block of code as long as a condition is `True`.

```python
while True:
    user_value = int(input("Enter a number above 10: "))
    if user_value > 10:
        print("Thanks!")
        break
    else:
        print("Try again.")
```

---

## 12. Recursion
File: [a-brief-intro-to-recursion.py](7-more-practice-control-flow/a-brief-intro-to-recursion.py)

Recursion is a technique where a function calls itself. I used it to implement a countdown.

```python
def count_down_from(number):
    if number <= 0:
        return
    print(number)
    count_down_from(number - 1)

count_down_from(5)  # Output: 5, 4, 3, 2, 1
```

---

## 13. String Reversal with Recursion
File: [a-brief-intro-to-recursion-II.py](7-more-practice-control-flow/a-brief-intro-to-recursion-II.py)

I implemented a recursive function to reverse a string.

```python
def reverse(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse(string[:-1])

print(reverse("straw"))  # Output: warts
```

---

## 14. Practice Problems
File: [assignment.py](7-more-practice-control-flow/assignment.py)

This section focuses on solving practical problems using control flow. Below are the functions I implemented:

### 14.1. Even or Odd
```python
def even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"

print(even_or_odd(2))  # Output: even
```

### 14.2. Truthy or Falsy
```python
def truthy_or_falsy(value):
    return "The value is truthy" if value else "The value is falsy"

print(truthy_or_falsy(0))  # Output: The value is falsy
```

### 14.3. Divisibility Check
```python
def divisible_by_three_and_four(number):
    return number % 3 == 0 and number % 4 == 0

print(divisible_by_three_and_four(12))  # Output: True
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of control flow in Python, including:
- Using `if`, `else`, and `elif` statements for decision-making.
- Combining conditions with `and`, `or`, and `not`.
- Evaluating truthy and falsy values with the `bool` function.
- Implementing loops with `while` and recursion for repeated execution.

These skills are essential for writing dynamic and interactive Python programs.