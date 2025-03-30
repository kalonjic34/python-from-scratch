
# In-depth: Strings Basics

This document provides a detailed summary of the key concepts and lessons I learned while exploring strings in Python. Strings are one of the most fundamental data types in Python, and understanding their behavior is essential for effective programming. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Length, Concatenation, and Immutability
File: [length-concatenation-and-immutability.py](5-more-practice-strings-the-basic/length-concatenation-and-immutability.py)

I learned how to calculate the length of strings using the `len()` function, concatenate strings, and understand the immutability of strings in Python.

```python
print(len("Python"))  # Output: 6
print("Chris" + " " + "Kalonji")  # Output: Chris Kalonji

# Strings are immutable, so the following line would raise an error:
# best_language_ever[0] = "B"
```

---

## 2. String Indexing with Positive Values
File: [string-indexing-with-positive-values.py](5-more-practice-strings-the-basic/string-indexing-with-positive-values.py)

String indexing allows access to individual characters using their position. Positive indices start from 0. I also learned about the immutability of strings and the behavior of out-of-range indices.

```python
best_language_ever = "Python"
print(best_language_ever[0])  # Output: P
print(best_language_ever[5])  # Output: n

# Accessing an out-of-range index raises an error:
# print(best_language_ever[100])  # IndexError
```

---

## 3. String Indexing with Negative Values
File: [string-indexing-with-negative-values.py](5-more-practice-strings-the-basic/string-indexing-with-negative-values.py)

Negative indexing starts from the end of the string, with `-1` representing the last character. This is useful for accessing characters relative to the end of the string.

```python
topic = "Programming"
print(topic[-1])  # Output: g
print(topic[-5])  # Output: a
```

---

## 4. String Slicing: By Range
File: [string-slicing-I-slicing-by-range.py](5-more-practice-strings-the-basic/string-slicing-I-slicing-by-range.py)

String slicing allows extracting substrings by specifying start and end indices. Omitting indices provides flexibility, such as slicing from the start or to the end of the string.

```python
address = "Adventures street, Beverly Hills, CA 90210"
print(address[0:10])  # Output: Adventures
print(address[:10])   # Output: Adventures
print(address[19:])   # Output: Beverly Hills, CA 90210
```

---

## 5. String Slicing: By Steps
File: [string-slicing-II-slicing-by-steps.py](5-more-practice-strings-the-basic/string-slicing-II-slicing-by-steps.py)

Slicing by steps allows skipping characters in the slice. Negative step values reverse the string or substring.

```python
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[0:10:2])  # Output: ACEGI
print(alphabet[::-1])    # Output: ZYXWVUTSRQPONMLKJIHGFEDCBA
```

---

## 6. Escape Characters
File: [escape-characters.py](5-more-practice-strings-the-basic/escape-characters.py)

Escape characters allow special formatting within strings, such as newlines, tabs, and quotes. I also learned about raw strings and multi-line statements.

```python
print("This will \nbegin on a \nnew line")  # Newline
print("\"To be or not to be\", said Hamlet")  # Escaped quotes
print(r"C:\\news\travel")  # Raw string
```

---

## 7. The `in` and `not in` Operators
File: [the-in-and-not-in-operators-for-inclusion-and-exclusion.py](5-more-practice-strings-the-basic/the-in-and-not-in-operators-for-inclusion-and-exclusion.py)

The `in` and `not in` operators check for the inclusion or exclusion of substrings within a string. These operators are useful for searching and filtering.

```python
announcement = "The winners of the prize are Chris, James, and Sam"
print("Chris" in announcement)  # Output: True
print("Steve" not in announcement)  # Output: True
```

---
## 8. String Manipulation Practice
File: [assignment.py](5-more-practice-strings-the-basic/assignment.py)

This section focuses on solving practical problems using string manipulation techniques. Below are the functions I implemented and what I learned from each:

### 8.1. Checking String Length
I created a function to check if a string has more than 7 characters. This demonstrates the use of the `len()` function to evaluate string length.

```python
def long_word(word):
    return len(word) > 7

print(long_word("Python"))       # Output: False
print(long_word("magnificent"))  # Output: True
```

---

### 8.2. Comparing String Lengths
I wrote a function to compare the lengths of two strings and determine if the first string is longer than the second. This highlights the use of `len()` for comparisons.

```python
def first_longer_than_second(first_word, second_word):
    return len(first_word) > len(second_word)

print(first_longer_than_second("Python", "Ruby"))  # Output: True
print(first_longer_than_second("cat", "mouse"))    # Output: False
```

---

### 8.3. Checking First and Last Characters
I implemented a function to check if the first and last characters of a string are the same. This demonstrates how to access characters using indexing.

```python
def same_first_and_last_letter(word):
    return word[0] == word[-1]

print(same_first_and_last_letter("runner"))  # Output: True
print(same_first_and_last_letter("clock"))   # Output: False
```

---

### 8.4. Summing Digits in a String
I created a function to calculate the sum of digits in a 3-character string. This required converting characters to integers using `int()`.

```python
def three_number_sum(wordsum):
    return int(wordsum[0]) + int(wordsum[1]) + int(wordsum[2])

print(three_number_sum("123"))  # Output: 6
print(three_number_sum("567"))  # Output: 18
```

---

### 8.5. Extracting Substrings
I wrote functions to extract specific parts of a string, such as the first 3 characters or the last 5 characters. This demonstrates slicing techniques.

```python
def first_three_characters(char):
    return char[0:3]

def last_five_characters(char):
    return char[-5:]

print(first_three_characters("dynasty"))  # Output: dyn
print(last_five_characters("dynasty"))    # Output: nasty
```

---

### 8.6. Checking for Palindromes
I implemented a function to check if a string is a palindrome (reads the same backward as forward). This demonstrates the use of slicing with a step of `-1` to reverse a string.

```python
def is_palindrome(word):
    return word[:] == word[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("yummy"))    # Output: False
```

---

### Summary of String Manipulation Practice
Through these exercises, I practiced:
- Using `len()` to evaluate string lengths.
- Comparing strings based on their lengths.
- Accessing specific characters using indexing.
- Extracting substrings with slicing.
- Reversing strings and checking for palindromes.
- Converting string characters to integers for arithmetic operations.

These exercises helped solidify my understanding of string manipulation and prepared me for solving real-world problems involving text data.

