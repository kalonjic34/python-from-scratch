# Tuples

This document provides a detailed summary of the key concepts and lessons I learned while exploring tuples in Python. Tuples are immutable sequences that are useful for storing collections of items. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Tuples
File: [intro-to-tuples.py](13-tuples/intro-to-tuples.py)

Tuples are immutable sequences that can store multiple items. They are defined using parentheses `()`.

```python
foods = ("Sushi", "Steak", "Guacamole")
print(type(foods))  # Output: <class 'tuple'>

empty = ()
print(type(empty))  # Output: <class 'tuple'>

mystery = (1,)
print(type(mystery))  # Output: <class 'tuple'>
```

---

## 2. Lists vs Tuples
File: [lists-vs-tuples.py](13-tuples/lists-vs-tuples.py)

Tuples are immutable, meaning their elements cannot be changed after creation. However, mutable objects within tuples can still be modified.

```python
birthday = (4, 15, 2000)
print(birthday[0])  # Output: 4

addresses = (
    ["Hudson Street", "New York", "NY"],
    ["Palmer Street", "Cape Town", "WC"]
)
addresses[1][0] = "Polk Street"
print(addresses)  # Output: (['Hudson Street', 'New York', 'NY'], ['Polk Street', 'Cape Town', 'WC'])
```

---

## 3. Unpacking a Tuple: The Basics
File: [unpacking-a-tuple-I-the-basics.py](13-tuples/unpacking-a-tuple-I-the-basics.py)

Tuple unpacking allows you to assign elements of a tuple to variables in a single statement.

```python
employee = ("Bob", "Johnson", "Manager", 50)
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)  # Output: Bob Johnson Manager 50
```

---

## 4. Unpacking a Tuple: Using `*` to Destructure Multiple Elements
File: [unpacking-a-tuple-II-using-_-to-destructure-multiple-elements.py](13-tuples/unpacking-a-tuple-II-using-_-to-destructure-multiple-elements.py)

The `*` operator can be used to unpack multiple elements into a list.

```python
employee = ("Bob", "Johnson", "Manager", 50)
first_name, *details, age = employee
print(details)  # Output: ['Johnson', 'Manager']
```

---

## 5. Unpacking Arguments to Functions
File: [unpacking-arguments-to-functions.py](13-tuples/unpacking-arguments-to-functions.py)

The `*` operator can also be used to unpack a tuple or list into function arguments.

```python
def product(a, b):
    return a * b

numbers = [3, 5]
print(product(*numbers))  # Output: 15
```

---

## 6. Variable Number of Function Arguments with `*args`
File: [variable-number-of-function-arguments-with-_args.py](13-tuples/variable-number-of-function-arguments-with-_args.py)

The `*args` syntax allows a function to accept a variable number of arguments.

```python
def accept_stuff(*args):
    print(args)

accept_stuff(1, 2, 3)  # Output: (1, 2, 3)
```

---

## 7. Practice Problems
File: [assignment.py](13-tuples/assignment.py)

This section focuses on solving practical problems using tuples. Below are the functions I implemented:

### 7.1. Create a Tuple of Months
```python
months = ("September", "October", "November", "December")
print(months)  # Output: ('September', 'October', 'November', 'December')
```

---

### 7.2. Convert a List to a Tuple
```python
faves = ["Inception", "American Gangster", "Good Will Hunting"]
movies = tuple(faves)
print(movies)  # Output: ('Inception', 'American Gangster', 'Good Will Hunting')
```

---

### 7.3. Combine Tuples
```python
numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)
all_numbers = numbers_a + numbers_b + numbers_c
print(all_numbers)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

---

### 7.4. Destructure a Tuple
```python
job_opening = ("Software Engineer", "Cape Town", 30000)
position, city, salary = job_opening
print(position)  # Output: Software Engineer
```

---

### 7.5. Evens and Odds
```python
def sum_of_evens_and_odd(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 == 1]
    return (sum(even_numbers), sum(odd_numbers))

print(sum_of_evens_and_odd((1, 2, 3, 4)))  # Output: (6, 4)
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of tuples in Python, including:
- Their immutability and use cases.
- Unpacking and destructuring tuples.
-# Tuples

This document provides a detailed summary of the key concepts and lessons I learned while exploring tuples in Python. Tuples are immutable sequences that are useful for storing collections of items. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Tuples
File: [intro-to-tuples.py](13-tuples/intro-to-tuples.py)

Tuples are immutable sequences that can store multiple items. They are defined using parentheses `()`.

```python
foods = ("Sushi", "Steak", "Guacamole")
print(type(foods))  # Output: <class 'tuple'>

empty = ()
print(type(empty))  # Output: <class 'tuple'>

mystery = (1,)
print(type(mystery))  # Output: <class 'tuple'>
```

---

## 2. Lists vs Tuples
File: [lists-vs-tuples.py](13-tuples/lists-vs-tuples.py)

Tuples are immutable, meaning their elements cannot be changed after creation. However, mutable objects within tuples can still be modified.

```python
birthday = (4, 15, 2000)
print(birthday[0])  # Output: 4

addresses = (
    ["Hudson Street", "New York", "NY"],
    ["Palmer Street", "Cape Town", "WC"]
)
addresses[1][0] = "Polk Street"
print(addresses)  # Output: (['Hudson Street', 'New York', 'NY'], ['Polk Street', 'Cape Town', 'WC'])
```

---

## 3. Unpacking a Tuple: The Basics
File: [unpacking-a-tuple-I-the-basics.py](13-tuples/unpacking-a-tuple-I-the-basics.py)

Tuple unpacking allows you to assign elements of a tuple to variables in a single statement.

```python
employee = ("Bob", "Johnson", "Manager", 50)
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)  # Output: Bob Johnson Manager 50
```

---

## 4. Unpacking a Tuple: Using `*` to Destructure Multiple Elements
File: [unpacking-a-tuple-II-using-_-to-destructure-multiple-elements.py](13-tuples/unpacking-a-tuple-II-using-_-to-destructure-multiple-elements.py)

The `*` operator can be used to unpack multiple elements into a list.

```python
employee = ("Bob", "Johnson", "Manager", 50)
first_name, *details, age = employee
print(details)  # Output: ['Johnson', 'Manager']
```

---

## 5. Unpacking Arguments to Functions
File: [unpacking-arguments-to-functions.py](13-tuples/unpacking-arguments-to-functions.py)

The `*` operator can also be used to unpack a tuple or list into function arguments.

```python
def product(a, b):
    return a * b

numbers = [3, 5]
print(product(*numbers))  # Output: 15
```

---

## 6. Variable Number of Function Arguments with `*args`
File: [variable-number-of-function-arguments-with-_args.py](13-tuples/variable-number-of-function-arguments-with-_args.py)

The `*args` syntax allows a function to accept a variable number of arguments.

```python
def accept_stuff(*args):
    print(args)

accept_stuff(1, 2, 3)  # Output: (1, 2, 3)
```

---

## 7. Practice Problems
File: [assignment.py](13-tuples/assignment.py)

This section focuses on solving practical problems using tuples. Below are the functions I implemented:

### 7.1. Create a Tuple of Months
```python
months = ("September", "October", "November", "December")
print(months)  # Output: ('September', 'October', 'November', 'December')
```

---

### 7.2. Convert a List to a Tuple
```python
faves = ["Inception", "American Gangster", "Good Will Hunting"]
movies = tuple(faves)
print(movies)  # Output: ('Inception', 'American Gangster', 'Good Will Hunting')
```

---

### 7.3. Combine Tuples
```python
numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)
all_numbers = numbers_a + numbers_b + numbers_c
print(all_numbers)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

---

### 7.4. Destructure a Tuple
```python
job_opening = ("Software Engineer", "Cape Town", 30000)
position, city, salary = job_opening
print(position)  # Output: Software Engineer
```

---

### 7.5. Evens and Odds
```python
def sum_of_evens_and_odd(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 == 1]
    return (sum(even_numbers), sum(odd_numbers))

print(sum_of_evens_and_odd((1, 2, 3, 4)))  # Output: (6, 4)
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of tuples in Python, including:
- Their immutability and use cases.
- Unpacking and destructuring tuples.
-