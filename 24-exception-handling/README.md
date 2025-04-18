# README: Exception Handling in Python

This document summarizes key concepts and examples related to exception handling in Python. Exception handling allows developers to manage errors gracefully and ensure that programs can continue running or fail softly.

---

## 1. User-Defined Exceptions
**File:** [user-defined-exceptions.py](user-defined-exceptions.py)

In this example, I defined a custom exception called `NegativeNumbersError` to handle cases where input numbers are negative.

```python
class NegativeNumbersError(Exception):
    """
    One or more inputs are negative
    """
    pass

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
    except NegativeNumbersError:
        return "Shame on you, not valid!"

print(add_positive_numbers(-5, -2))  # Output: Shame on you, not valid!
```

**Key Insights:**
- **Custom exceptions** enhance code readability and maintainability by allowing developers to define clear error messages relevant to their application's context. This specificity helps in debugging and understanding issues that arise during execution.
- Using custom exceptions promotes **better error handling strategies** tailored to specific application needs, reducing the likelihood of generic error messages that may confuse users.

---

## 2. The Try-Except Block
**File:** [the-try-except-block.py](the-try-except-block.py)

This example demonstrates the basic try-except block to handle exceptions during division.

```python
def divide_five_by_number(n):
    try:
        return 5 / n
    except:
        pass

print(divide_five_by_number(0))        # Output: None
print(divide_five_by_number(10))       # Output: 0.5
print(divide_five_by_number("Nonsense"))  # Output: None
```

**Key Insights:**
- The **try-except structure** provides a way to catch exceptions, allowing the program to continue running instead of crashing. This is crucial for maintaining user experience and application stability.
- A **bare `except`** can catch all exceptions, but it is a best practice to specify the exception type to avoid hiding unexpected errors, which can lead to debugging difficulties.

---

## 3. The Raise Keyword
**File:** [the-raise-keyword.py](the-raise-keyword.py)

In this example, I used the `raise` keyword to trigger a `ValueError` if inputs are not positive.

```python
def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or both of the values is invalid. Both numbers must be positive")
        
        return a + b 
    except ValueError as e:
        return f"Caught the ValueError: {e}"

print(add_positive_numbers(10, 5))  # Output: 15
print(add_positive_numbers(-2, 3))  # Output: Caught the ValueError: One or both of the values is invalid. Both numbers must be positive
```

**Key Insights:**
- The `raise` keyword allows for **intentional exception generation**, which can be useful for enforcing business rules or validating conditions before proceeding with operations.
- Raising exceptions with **descriptive messages** improves the clarity of errors, making it easier for users and developers to understand what went wrong and why.

---

## 4. The Else and Finally Blocks
**File:** [the-else-and-finally-blocks.py](the-else-and-finally-blocks.py)

This example illustrates the use of `else` and `finally` blocks in exception handling.

```python
x = 10

try:
    print(x + 5)
except NameError:
    print("Some variable is not defined!")    
else:
    print("This will print if there is no error in the try.")
finally:
    print("This will print with or without exception")
    print("Closing File...")
```

**Key Insights:**
- The `else` block executes if no exceptions are raised in the `try` block, allowing for **additional logic** to be executed when the operation is successful.
- The `finally` block ensures that **cleanup actions** (like closing files or releasing resources) are performed regardless of whether an exception occurred, ensuring that the program can manage resources effectively.

---

## 5. Exception Inheritance Hierarchies
**File:** [exception-inheritance-hierarchies.py](exception-inheritance-hierarchies.py)

This example demonstrates creating a hierarchy of custom exceptions.

```python
class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
    print(f"Caught the error: {e}")

try:
    raise StupidMistake("Extra stupid mistake")
except Mistake as e:
    print(f"Caught the error: {e}")

try:
    raise StupidMistake("Super stupid mistake")
except Mistake as e:
    print(f"Caught the error: {e}")
```

**Key Insights:**
- Custom exception hierarchies allow for **organized error management**, grouping related exceptions under a common base class. This makes it easier to handle multiple related errors with a single exception handler.
- Inheritance in exceptions promotes **code reuse**, reducing duplication and enhancing the maintainability of error handling logic across the application.

---

## 6. Catching One or More Specific Exceptions
**File:** [catching-one-or-more-specific-exceptions.py](catching-one-or-more-specific-exceptions.py)

In this example, I handle multiple specific exceptions when performing division.

```python
def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was {e}"
        
    return calculation

print(divide_five_by_number(10))         # Output: 0.5
print(divide_five_by_number(0))          # Output: Something went wrong. The error was division by zero
print(divide_five_by_number("nonsense"))  # Output: Something went wrong. The error was unsupported operand type(s) for /
```

**Key Insights:**
- Catching multiple exceptions can be done using a **tuple**, allowing for streamlined error handling when several types of errors can occur from the same block of code.
- This approach helps in writing **cleaner code**, as it reduces the need for multiple `except` blocks for similar error handling logic, promoting efficiency and readability.

---

## Summary

I've gained a comprehensive understanding of:
- User-defined exceptions and their importance.
- Basic try-except blocks and their usage.
- The `raise` keyword for intentional exception handling.
- The roles of `else` and `finally` in exception handling.
- Organizing exceptions into inheritance hierarchies.
- Catching multiple specific exceptions.

These concepts are essential for writing robust, error-resistant Python code.