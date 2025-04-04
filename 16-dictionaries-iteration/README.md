# Dictionaries: Iteration

This document provides a detailed summary of the key concepts and lessons I learned while iterating over dictionaries in Python. Iterating through dictionaries allows for efficient access and manipulation of keys, values, and key-value pairs. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Iterating Over a Dictionary with a `for` Loop
File: [iterate-over-a-dictionary-with-a-for-loop.py](16-dictionaries-iteration/iterate-over-a-dictionary-with-a-for-loop.py)

You can iterate over a dictionary's keys and access their corresponding values using a `for` loop.

```python
chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Ribs": 7.99,
    "Fried Rice": 1.99
}

for food in chinese_food:
    print(f"The food is {food} and price is {chinese_food[food]}")
```

---

## 2. The `items` Method
File: [the-items-method.py](16-dictionaries-iteration/the-items-method.py)

The `items` method returns a view object of key-value pairs, which can be iterated over in a `for` loop.

```python
college_course = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein"
}

for course, professor in college_course.items():
    print(f"The course {course} is being taught by {professor}")
```

---

## 3. The `keys` and `values` Methods
File: [the-keys-and-values-methods.py](16-dictionaries-iteration/the-keys-and-values-methods.py)

The `keys` method returns a view object of all keys, while the `values` method returns a view object of all values.

```python
cryptocurrency_prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

for currency in cryptocurrency_prices.keys():
    print(f"The next currency is {currency}")

for price in cryptocurrency_prices.values():
    print(f"The next price is {price}")
```

---

## 4. The `sorted` Function
File: [the-sorted-function.py](16-dictionaries-iteration/the-sorted-function.py)

The `sorted` function can be used to iterate over a dictionary's keys or items in sorted order.

```python
wheel_count = {
    "truck": 4,
    "car": 2,
    "bus": 8
}

for vehicle, count in sorted(wheel_count.items()):
    print(f"The next vehicle is a {vehicle} and it has {count} wheels.")
```

---

## 5. Dictionary Comprehensions: Basics
File: [dictionary-comprehensions-I.py](16-dictionaries-iteration/dictionary-comprehensions-I.py)

Dictionary comprehensions provide a concise way to create dictionaries from iterables.

```python
languages = ["Python", "JavaScript", "Ruby"]
lengths = {language: len(language) for language in languages if "t" in language}
print(lengths)  # Output: {'Python': 6, 'JavaScript': 10}
```

---

## 6. Dictionary Comprehensions: Advanced
File: [dictionary-comprehensions-II.py](16-dictionaries-iteration/dictionary-comprehensions-II.py)

You can use dictionary comprehensions with conditions to invert dictionaries or filter key-value pairs.

```python
capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
}

inverted = {capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(inverted)  # Output: {'Albany': 'New York', 'Sacramento': 'California'}
```

---

## 7. Unpacking Argument Dictionaries
File: [unpacking-argument-dictionary.py](16-dictionaries-iteration/unpacking-argument-dictionary.py)

The `**` operator can be used to unpack a dictionary into function arguments.

```python
def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

stats = {"feet": 5, "inches": 11}
print(height_to_meters(**stats))  # Output: 1.8034
```

---

## 8. Keyword Arguments (`**kwargs`)
File: [keyword-arguments-kwargs.py](16-dictionaries-iteration/keyword-arguments-kwargs.py)

The `**kwargs` syntax allows a function to accept an arbitrary number of keyword arguments.

```python
def collect_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}")

collect_keyword_arguments(a=2, b=3, c=4)
```

---

## 9. Lists of Dictionaries
File: [lists-of-dictionaries.py](16-dictionaries-iteration/lists-of-dictionaries.py)

You can iterate over a list of dictionaries to access and manipulate their key-value pairs.

```python
concert_attendees = [
    {"Name": "Sam", "Section": 400, "Price Paid": 99.99},
    {"Name": "Ian", "Section": 223, "Price Paid": 149.99}
]

for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}")
```

---

## 10. Practice Problems
File: [assignment.py](16-dictionaries-iteration/assignment.py)

This section focuses on solving practical problems using dictionary iteration. Below are some examples:

### 10.1. Invert a Dictionary
```python
def invert_function(my_dict):
    return {value: key for key, value in my_dict.items()}

print(invert_function({'A': 'B', 'C': 'D'}))  # Output: {'B': 'A', 'D': 'C'}
```

### 10.2. Sum of Values
```python
def sum_of_values(dictionary, keys):
    return sum(dictionary[key] for key in keys if key in dictionary)

print(sum_of_values({'a': 5, 'b': 3, 'c': 10}, ["a", "c"]))  # Output: 15
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- Iterating over keys, values, and key-value pairs in dictionaries.
- Using dictionary comprehensions for concise dictionary creation.
- Unpacking dictionaries into function arguments.
- Solving practical problems using dictionary iteration.

These techniques are essential for working with dictionaries efficiently in Python.