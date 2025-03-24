# Python Basics: What I Learned

This document summarizes the key concepts and lessons I learned while working through the "Introduction to Python" exercises.

---

## 1. Hello World and Basic Printing
File: [helloworld.py](1-introduction-to-python/helloworld.py)

- Learned how to print basic strings and numbers.
- Explored combining multiple arguments in a `print()` statement.
- Example:
  ```python
  print('Hello, World!')
  print(1 + 2)
  print("The end", "or is it?", "keep coding to learn more about Python", 3)
  ```

---

## 2. Operators
File: [operators.py](1-introduction-to-python/operators.py)

- Learned about arithmetic operators:
  - Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
  - Integer division (`//`) and Modulus (`%`).
- Explored operator precedence and grouping with parentheses.
- Example:
  ```python
  a = 12
  b = 3
  print(a + b)  # 15
  print(a // b)  # 4
  print(a + (b / 3) - (4 * 12))
  ```

---

## 3. Strings and Escape Characters
File: [char.py](1-introduction-to-python/char.py)

- Learned about escape characters like `\n` (newline) and `\t` (tab).
- Explored raw strings with `r""` to avoid escaping backslashes.
- Example:
  ```python
  splitString = 'This string has been\nsplit over\nseveral\nlines'
  print(r"C:\Users\christian\notes.txt")
  ```

---

## 4. String Slicing and Indexing
File: [strings2.py](1-introduction-to-python/strings2.py)

- Learned how to slice strings using `[start:end:step]`.
- Explored negative indexing to access characters from the end of a string.
- Example:
  ```python
  parrot = 'Norwegian Blue'
  print(parrot[0:6])  # Norweg
  print(parrot[-4:])  # Blue
  ```

---

## 5. String Formatting with `.format()`
File: [repfields.py](1-introduction-to-python/repfields.py)

- Learned how to use `.format()` for string interpolation.
- Explored positional arguments and reusing placeholders.
- Example:
  ```python
  age = 24
  print("My age is {0} years".format(age))
  print("Jan: {2}, Feb: {0}, Mar: {1}".format(23, 30, 27))
  ```

---

## 6. Advanced String Formatting
File: [formatting.py](1-introduction-to-python/formatting.py)

- Learned about alignment and precision in string formatting.
- Explored left (`<`), right (`>`), and center (`^`) alignment.
- Example:
  ```python
  for i in range(1, 13):
      print("No. {0:2} squared is {1:<3} and cube is {2:^4}".format(i, i**2, i**3))
  ```

---

## 7. String Interpolation with `%`
File: [interpolation.py](1-introduction-to-python/interpolation.py)

- Learned about the old-style string interpolation using `%`.
- Explored formatting integers (`%d`), strings (`%s`), and floats (`%f`).
- Example:
  ```python
  age = 24
  print("My age is %d years" % age)
  print("Pi is approx %60.50f" % (22 / 7))
  ```

---

## 8. Working with Sequences
File: [sequence_operators.py](1-introduction-to-python/sequence_operators.py)

- Learned about string concatenation and repetition.
- Explored membership operators (`in` and `not in`).
- Example:
  ```python
  string1 = "he's "
  string2 = "probably "
  print(string1 + string2)
  print("Hello " * 5)
  print("day" in "friday")  # True
  ```

---

## 9. String Slicing and Reversing
File: [sliceback.py](1-introduction-to-python/sliceback.py)

- Learned how to reverse strings using slicing.
- Explored slicing with negative steps.
- Example:
  ```python
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print(letters[::-1])  # Reverse the string
  print(letters[16:13:-1])  # qpo
  ```

---

## 10. String Basics and Concatenation
File: [strings.py](1-introduction-to-python/strings.py)

- Learned about basic string operations and concatenation.
- Explored f-strings for embedding variables in strings.
- Example:
  ```python
  greeting = 'Hello'
  name = 'Chris'
  print(f"{greeting} {name}")
  print(f"Pi is approx {22 / 7:12.50f}")
  ```

---

## Summary
Through these exercises, I gained a solid understanding of Python basics, including:
- Printing and formatting strings.
- Using operators and understanding precedence.
- Working with strings, slicing, and indexing.
- String interpolation using `.format()`, `%`, and f-strings.
- Advanced formatting techniques for alignment and precision.

This foundational knowledge sets the stage for more advanced Python programming