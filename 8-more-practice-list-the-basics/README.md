# In-depth: List Basics

This document provides a detailed summary of the key concepts and lessons I learned while exploring lists in Python. Lists are one of the most versatile and commonly used data structures in Python, allowing us to store and manipulate collections of items. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Lists
File: [intro-to-lists.py](8-more-practice-list-the-basics/intro-to-lists.py)

Lists are ordered collections of items that can store elements of different data types. I learned how to create lists, check their length using the `len()` function, and explore their versatility.

```python
sodas = ["coke", "Pepsi", "Dr. Pepper"]
print(len(sodas))  # Output: 3

quarterly_revenues = [15000, 12000, 9000, 20000]
print(len(quarterly_revenues))  # Output: 4
```

---

## 2. Selecting List Elements by Index
File: [select-a-list-element-by-positive-or-negative-index-positions.py](8-more-practice-list-the-basics/select-a-list-element-by-positive-or-negative-index-positions.py)

Lists support indexing to access individual elements. Positive indices start from the beginning, while negative indices start from the end.

```python
web_browser = ["Chrome", "Firefox", "Safari", "Opera", "Edge"]
print(web_browser[0])  # Output: Chrome
print(web_browser[-1])  # Output: Edge
```

---

## 3. Slicing Multiple Elements from a List
File: [slice-multiple-elements-from-a-list.py](8-more-practice-list-the-basics/slice-multiple-elements-from-a-list.py)

Slicing allows us to extract multiple elements from a list by specifying a range of indices. I also learned how to use step values and reverse a list using slicing.

```python
muscles = ["Biceps", "Triceps", "Deltoid", "Sartorius"]
print(muscles[1:3])  # Output: ['Triceps', 'Deltoid']
print(muscles[::-1])  # Output: ['Sartorius', 'Deltoid', 'Triceps', 'Biceps']
```

---

## 4. The `in` and `not in` Operators on a List
File: [the-in-and-not-in-operators-on-a-list.py](8-more-practice-list-the-basics/the-in-and-not-in-operators-on-a-list.py)

The `in` and `not in` operators check for the presence or absence of an element in a list.

```python
meals = ["breakfast", "lunch", "dinner"]
print("lunch" in meals)  # Output: True
print("snack" not in meals)  # Output: True
```

---

## 5. Practice Problems
File: [assignment.py](8-more-practice-list-the-basics/assignment.py)

This section focuses on solving practical problems using lists. Below are the functions I implemented:

### 5.1. Checking List Length
I created a function to check if a list has more than 5 elements.

```python
def is_long(elements):
    return len(elements) > 5

print(is_long([1, 2, 3]))  # Output: False
print(is_long([1, 2, 3, 4, 5, 6]))  # Output: True
```

---

### 5.2. Concatenating First and Last Elements
I wrote a function to concatenate the first and last elements of a list of strings.

```python
def first_and_last(elements):
    return elements[0] + elements[-1]

print(first_and_last(["a", "b", "c"]))  # Output: ac
```

---

### 5.3. Product of Even Indices
I implemented a function to calculate the product of elements at even indices in a list of 6 numbers.

```python
def product_of_even_indices(numbers):
    return numbers[0] * numbers[2] * numbers[4]

print(product_of_even_indices([1, 2, 3, 4, 5, 6]))  # Output: 15
```

---

### 5.4. First Letter of Last String
I created a function to return the first letter of the last string in a list.

```python
def first_letter_of_last_string(elements):
    return elements[-1][0]

print(first_letter_of_last_string(["cat", "dog", "zebra"]))  # Output: z
```

---

### 5.5. Splitting a List Based on a Number
I wrote a function to split a list into two parts based on whether a number is even or odd.

```python
def split_in_two(elements, number):
    if number % 2 == 0:
        return elements[2:]
    else:
        return elements[:2]

elements = ["a", "b", "c", "d", "e", "f"]
print(split_in_two(elements, 3))  # Output: ['a', 'b']
```

---

### 5.6. Nested List Extraction
I implemented a function to extract an element from a nested list based on an index.

```python
def nested_extraction(nl, index):
    return nl[index][index]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 1))  # Output: 8
```

---

### 5.7. Checking First and Last Elements
I created a function to check if the first and last elements of a list are equal.

```python
def beginning_and_end(elements):
    return elements[0] == elements[-1]

print(beginning_and_end([1, 2, 3, 1]))  # Output: True
```

---

### 5.8. Checking for a Long Word in a List
I wrote a function to check if a word exists in a list and has more than 4 characters.

```python
def long_word_in_collection(elements, target):
    return target in elements and len(target) > 4

elements = ["cat", "dog", "rhino"]
print(long_word_in_collection(elements, "rhino"))  # Output: True
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of lists in Python, including:
- Creating and manipulating lists.
- Accessing elements using positive and negative indices.
- Extracting multiple elements with slicing.
- Checking for membership using `in` and `not in`.
- Solving practical problems using lists.

These skills are essential for working with collections of data in Python and form the foundation for more advanced list operations.