# In-depth: Strings Methods

This document provides a detailed summary of the key concepts and lessons I learned while exploring string methods in Python. String methods are built-in functions that allow us to manipulate and analyze strings effectively. Below is a breakdown of the topics covered and the insights gained.

---

## 1. The `capitalize`, `title`, `lower`, `upper`, and `swapcase` Methods
File: [the-capitalize-title-lower-upper-and-swapcase-methods.py](6-more-practice-strings-methods/the-capitalize-title-lower-upper-and-swapcase-methods.py)

These methods allow us to transform the case of strings in various ways. I learned how to capitalize the first letter, convert strings to title case, and swap the case of characters.

```python
story = "once upon a time"

print(story.capitalize())  # Output: Once upon a time
print(story.title())       # Output: Once Upon A Time
print(story.upper())       # Output: ONCE UPON A TIME
print("HELLO".lower())     # Output: hello
print("AbCdE".swapcase())  # Output: aBcDe
```

---

## 2. Boolean Methods for Strings
File: [boolean-methods-for-strings.py](6-more-practice-strings-methods/boolean-methods-for-strings.py)

Boolean methods check specific properties of strings and return `True` or `False`. I explored methods like `islower`, `isupper`, `istitle`, `isalpha`, `isnumeric`, `isalnum`, and `isspace`.

```python
print("winter".islower())  # Output: True
print("SUMMER".isupper())  # Output: True
print("The Four Seasons".istitle())  # Output: True
print("Area".isalpha())  # Output: True
print("51".isnumeric())  # Output: True
print("Area51".isalnum())  # Output: True
print(" ".isspace())  # Output: True
```

---

## 3. The `strip`, `lstrip`, and `rstrip` Methods
File: [the-lstrip-rstrip-and-strip-methods.py](6-more-practice-strings-methods/the-lstrip-rstrip-and-strip-methods.py)

These methods remove whitespace or specified characters from the beginning, end, or both sides of a string. I learned how to clean up strings effectively.

```python
empty_space = "         content             "
print(empty_space.strip())  # Output: "content"
print(empty_space.lstrip())  # Output: "content             "
print(empty_space.rstrip())  # Output: "         content"
```

---

## 4. The `replace` Method
File: [the-replace-method.py](6-more-practice-strings-methods/the-replace-method.py)

The `replace` method replaces occurrences of a substring with another substring. I learned how to use it for string modifications.

```python
phone_number = "071 446 7780"
print(phone_number.replace(" ", "-"))  # Output: 071-446-7780
print(phone_number.replace("4", "3"))  # Output: 071 336 7780
```

---

## 5. The `count` Method
File: [the-count-method.py](6-more-practice-strings-methods/the-count-method.py)

The `count` method counts the occurrences of a substring in a string. I used it to analyze the frequency of characters or substrings.

```python
word = "queueing"
print(word.count("e"))  # Output: 3
print(word.count("ue"))  # Output: 2
print(word.count("z"))  # Output: 0
```

---

## 6. The `startswith` and `endswith` Methods
File: [the-startswith-and-endswith-methods.py](6-more-practice-strings-methods/the-startswith-and-endswith-methods.py)

These methods check if a string starts or ends with a specific substring. I learned how to use them for validation and filtering.

```python
salutation = "Mr. Kermit the Frog"
print(salutation.startswith("Mr"))  # Output: True
print(salutation.endswith("Frog"))  # Output: True
```

---

## 7. The `find` and `index` Methods
File: [the-find-and-index-methods.py](6-more-practice-strings-methods/the-find-and-index-methods.py)

The `find` method locates the first occurrence of a substring and returns its index or `-1` if not found. The `index` method is similar but raises a `ValueError` if the substring is not found.

```python
browser = "Google Chrome"
print(browser.find("C"))  # Output: 7
print(browser.index("C"))  # Output: 7
# print(browser.index("Z"))  # Raises ValueError
```

---

## 8. The `format` Method
File: [the-format-method.py](6-more-practice-strings-methods/the-format-method.py)

The `format` method allows us to insert values into placeholders within a string. I learned how to use both positional and keyword arguments.

```python
mad_libs = "{name} laughed at the {adjective} {noun}."
print(mad_libs.format(name="Robby", adjective="green", noun="alien"))
# Output: Robby laughed at the green alien
```

---

## 9. Formatted String Literals (f-strings)
File: [formatted-string-literals.py](6-more-practice-strings-methods/formatted-string-literals.py)

Formatted string literals (f-strings) provide a concise way to embed expressions inside string literals. I learned how to use them for dynamic string creation.

```python
name = "Robby"
adjective = "green"
noun = "alien"
print(f"{name} laughed at the {adjective} {noun}")
# Output: Robby laughed at the green alien
```

---

## 10. String Manipulation Practice
File: [assignment.py](6-more-practice-strings-methods/assignment.py)

This section focuses on solving practical problems using string methods. Below are the functions I implemented and what I learned from each:

### 10.1. Counting Vowels
I created a function to count the number of vowels in a string using the `count` method.

```python
def vowel_count(word):
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")

print(vowel_count("estate"))  # Output: 3
print(vowel_count("helicopter"))  # Output: 4
```

---

### 10.2. Finding a Character's Index
I wrote a function to find the first index of a character in a string using the `find` method.

```python
def find_my_letter(string, char):
    return string.find(char)

print(find_my_letter("dangerous", "a"))  # Output: 1
print(find_my_letter("bazooka", "z"))  # Output: 2
```

---

### 10.3. Cleaning and Replacing Characters
I implemented a function to clean up whitespace and replace specific characters using `strip` and `replace`.

```python
def fancy_cleanup(word):
    return word.strip().replace("g", "z").replace(" ", "!")

print(fancy_cleanup("     geronimo crikey     "))  # Output: "zeronimo!crikey"
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of string methods in Python, including:
- Transforming string case with methods like `capitalize`, `title`, and `swapcase`.
- Validating string properties using boolean methods like `islower` and `isalpha`.
- Cleaning and modifying strings with methods like `strip`, `replace`, and `count`.
- Searching for substrings with `find`, `index`, `startswith`, and `endswith`.
- Dynamically formatting strings using `format` and f-strings.

These skills are essential for working with text data and solving real-world problems involving strings.