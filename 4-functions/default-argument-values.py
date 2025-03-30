def add(a = 0,b = 0):
    def add(a=0, b=0):
        """
        Adds two numbers together with default argument values.

        Parameters:
        a (int, optional): The first number to add. Defaults to 0.
        b (int, optional): The second number to add. Defaults to 0.

        Returns:
        int: The sum of the two numbers.

        Notes:
        - You have provided default values for both parameters, making them optional.
        - If no arguments are passed, the function will return 0 (default values added together).
        - This is a simple and effective use of default argument values in Python.
        """
    return a + b

print(add(7,8))
print(add(10))
print(add())
