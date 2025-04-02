# Built-in Functions

This document provides a detailed summary of the key concepts and lessons I learned while exploring Python's built-in functions. These functions are essential tools for performing common tasks efficiently. Below is a breakdown of the topics covered and the insights gained.

---

## 1. The `format` Function
File: [the-format-function.py](12-built-in-functions/the-format-function.py)

The `format` function formats values into strings with specified precision and styles.

```python
number = 0.123456789
print(format(number, ".2f"))  # Output: 0.12
print(format(123456, ","))   # Output: 123,456
print(format(0.5, ".2%"))    # Output: 50.00%
```

---

## 2. The `dir` Function
File: [the-dir-function.py](12-built-in-functions/the-dir-function.py)

The `dir` function returns a list of attributes and methods associated with an object.

```python
print(dir("pasta"))  # Output: ['__add__', '__class__', ..., '__len__', '__contains__']
print("pasta".__len__())  # Output: 5
```

---

## 3. The `sum` Function
File: [the-sum-function.py](12-built-in-functions/the-sum-function.py)

The `sum` function calculates the total of all elements in an iterable.

```python
print(sum([2, 3, 4]))  # Output: 9
print(sum([-1.3, 4.3, 7.34]))  # Output: 10.34
```

---

## 4. The `max` and `min` Functions
File: [the-max-and-min-functions.py](12-built-in-functions/the-max-and-min-functions.py)

The `max` and `min` functions return the largest and smallest elements in an iterable, respectively.

```python
print(max(3, 5, 7))  # Output: 7
print(min(["D", "Z", "K"]))  # Output: D
```

---

## 5. The `all` and `any` Functions
File: [the-all-and-any-functions.py](12-built-in-functions/the-all-and-any-functions.py)

The `all` function checks if all elements in an iterable are truthy, while `any` checks if at least one element is truthy.

```python
print(all([True, True, False]))  # Output: False
print(any([0, 1]))  # Output: True
```

---

## 6. Lambda Functions with `filter` and `map`
File: [lambda-functions.py](12-built-in-functions/lambda-functions.py)

Lambda functions are anonymous functions often used with `filter` and `map` for concise operations.

```python
metals = ["gold", "silver", "platinum"]
print(list(filter(lambda metal: len(metal) > 5, metals)))  # Output: ['silver', 'platinum']
print(list(map(lambda word: word.count("l"), metals)))    # Output: [1, 1, 1]
```

---

## 7. The `filter` Function
File: [the-filter-function.py](12-built-in-functions/the-filter-function.py)

The `filter` function filters elements from an iterable based on a condition.

```python
animals = ["elephant", "cat", "giraffe"]
print(list(filter(lambda animal: len(animal) > 5, animals)))  # Output: ['elephant', 'giraffe']
```

---

## 8. The `map` Function
File: [the-map-function.py](12-built-in-functions/the-map-function.py)

The `map` function applies a function to each element in an iterable.

```python
numbers = [4, 8, 15]
print(list(map(lambda x: x ** 3, numbers)))  # Output: [64, 512, 3375]
```

---

## 9. The `help` Function
File: [the-help-function.py](12-built-in-functions/the-help-function.py)

The `help` function displays documentation for Python objects, functions, and modules.

```python
help(len)  # Displays documentation for the `len` function
help("Hello".replace)  # Displays documentation for the `replace` method
```

---

## 10. Practice Problems
File: [assignment.py](12-built-in-functions/assignment.py)

This section focuses on solving practical problems using built-in functions. Below are the functions I implemented:

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

Through these exercises, I gained a comprehensive understanding of Python's built-in functions, including:
- Formatting, inspecting, and manipulating data.
- Filtering and mapping iterables with concise logic.
- Exploring Python's documentation using `help`.
- Solving practical problems with built-in functions.

These functions are powerful tools for writing efficient and readable Python code.