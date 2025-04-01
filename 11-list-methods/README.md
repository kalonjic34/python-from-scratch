# List: Methods

This document provides a detailed summary of the key concepts and lessons I learned while exploring list methods in Python. List methods are built-in functions that allow us to manipulate and analyze lists effectively. Below is a breakdown of the topics covered and the insights gained.

---

## 1. The `count` Method
File: [the-count-method.py](11-list-methods/the-count-method.py)

The `count` method returns the number of occurrences of a specified value in a list.

```python
car_lot = ["Ford", "Dodge", "Toyota", "Toyota", "Chevrolet", "Ford"]
print(car_lot.count("Toyota"))  # Output: 2
print(car_lot.count("Ferrari"))  # Output: 0
```

---

## 2. The `index` Method
File: [the-index-method.py](11-list-methods/the-index-method.py)

The `index` method returns the first index of a specified value in a list. It can also accept optional start and end parameters.

```python
pizzas = ["Mushroom", "Pepperoni", "Sausage", "Barbecue Chicken"]
print(pizzas.index("Pepperoni"))  # Output: 1
print(pizzas.index("Sausage", 2))  # Output: 2
```

---

## 3. The `copy` Method
File: [the-copy-method.py](11-list-methods/the-copy-method.py)

The `copy` method creates a shallow copy of a list. I also explored slicing as an alternative way to copy a list.

```python
units = ["Meter", "Kilogram", "Second"]
more_units = units.copy()
units.remove("Kilogram")
print(units)  # Output: ['Meter', 'Second']
print(more_units)  # Output: ['Meter', 'Kilogram', 'Second']
```

---

## 4. The `split` Method on a String
File: [the-split-method-on-a-string.py](11-list-methods/the-split-method-on-a-string.py)

The `split` method splits a string into a list of substrings based on a specified delimiter.

```python
users = "Bob, Dave, John, Sue"
print(users.split(", "))  # Output: ['Bob', 'Dave', 'John', 'Sue']
```

---

## 5. The `join` Method on a String
File: [the-join-method-on-a-string.py](11-list-methods/the-join-method-on-a-string.py)

The `join` method combines elements of a list into a single string, separated by a specified delimiter.

```python
address = ["500 Fifth Avenue", "New York", "NY", "10036"]
print(", ".join(address))  # Output: 500 Fifth Avenue, New York, NY, 10036
```

---

## 6. The `zip` Function
File: [the-zip-function.py](11-list-methods/the-zip-function.py)

The `zip` function combines multiple lists into tuples, pairing elements by their index.

```python
breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meals: {breakfast}, {lunch}, {dinner}")
```

---

## 7. Multidimensional Lists
File: [multidimensional-lists.py](11-list-methods/multidimensional-lists.py)

I explored lists of lists and how to access and iterate through their elements.

```python
bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry"],
    ["Kiwi", "Chocolate"]
]

print(bubble_tea_flavors[1][2])  # Output: Strawberry
```

---

## 8. List Comprehensions: Basics
File: [list-comprehensions-I-the-basics.py](11-list-methods/list-comprehensions-I-the-basics.py)

List comprehensions provide a concise way to create lists by applying an expression to each element in an iterable.

```python
numbers = [3, 4, 5, 6, 7]
squares = [number ** 2 for number in numbers]
print(squares)  # Output: [9, 16, 25, 36, 49]
```

---

## 9. List Comprehensions: Filtering
File: [list-comprehensions-II-filtering.py](11-list-methods/list-comprehensions-II-filtering.py)

I learned how to use list comprehensions with conditional logic to filter elements.

```python
donuts = ["Boston Cream", "Jelly", "Vanilla Cream", "Glazed"]
creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)  # Output: ['Boston Cream', 'Vanilla Cream']
```

---

## 10. Practice Problems
File: [assignment.py](11-list-methods/assignment.py)

This section focuses on solving practical problems using list methods. Below are the functions I implemented:

### 10.1. Encrypting a Message
```python
def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabet[(alphabet.index(letter) + 2) % 26] for letter in message])

print(encrypt_message("abc"))  # Output: cde
```

---

### 10.2. Word Lengths
```python
def word_lengths(string):
    return [len(word) for word in string.split(" ")]

print(word_lengths("Mary Poppins was a nanny"))  # Output: [4, 7, 3, 1, 5]
```

---

### 10.3. Cleaning Up Strings
```python
def cleanup(strings):
    return " ".join([string for string in strings if string.strip()])

print(cleanup(["cat", "", "er", "pillar"]))  # Output: cat er pillar
```

---

### 10.4. Nested Sum
```python
def nested_sum(numbers):
    return sum([sum(sublist) for sublist in numbers])

print(nested_sum([[1, 2], [3], [4, 5]]))  # Output: 15
```

---

### 10.5. Fancy Concatenate
```python
def fancy_concatenate(strings):
    return "".join(["".join(sublist) for sublist in strings if len(sublist) == 3])

print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))  # Output: ABC
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of list methods in Python, including:
- Counting, indexing, and copying elements.
- Splitting and joining strings.
- Using multidimensional lists and list comprehensions.
- Solving practical problems with list methods.

These skills are essential for working with and manipulating lists in Python.