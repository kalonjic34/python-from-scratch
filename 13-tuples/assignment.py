# Create a list with the last 4 months of the year (September, October, November, December)
# as strings. Ensure the first letter of each month is capitalized.

months = ("september", "october", "november", "december")
print(months)

# Create a variable with a list of your 3 favorite movies.
# Use a function to convert the list to a tuple and save the result in a movies variable.

faves = ["Inception", "American Gangster","Good Will Hunting"]
movies =tuple(faves)
print(movies)

# Create variables numbers_a, numbers_b, and numbers_c as tuples.
# Each should contain 3 integers.
# Create a numbers variable as a tuple containing these three tuples.

numbers_a = (1,2,3)
numbers_b = (4,5,6)
numbers_c = (7,8,9)

all_numbers = numbers_a + numbers_b + numbers_c
print(all_numbers)

# Given below, destructure the three values and assign them to position, city, and salary variables.
# The position should contain job titles (e.g., "Software Engineer"), city should contain city names
# (e.g., "New York City"), and salary should be a number (e.g., 100000).

job_opening = ("Software Engineer", "Cape Town", 30000)
position, setting, salary = job_opening

# Below, the first value and assign it to a street variable
# the second value and assign it to a zip_code variable
# the last value into a list and assign it to a city.

address = ("34 Elm Street", "Cape Town", "WC", "8000")

street, *city_and_state, zip_code = address
print(street)
print(city_and_state)
print(zip_code)

# Define an evens_and_odds function that accepts a tuple of numbers.
# Return a tuple with two numeric values:
#    the count of even numbers
#    the count of odd numbers.

def sum_of_evens_and_odd(numbers):
    even_numbers = [number for number in numbers if number % 2 ==0]
    odd_numbers = [number for number in numbers if number % 2 ==1]
    
    return (sum(even_numbers), sum(odd_numbers))

print(sum_of_evens_and_odd((1,2,3,4)))
print(sum_of_evens_and_odd((1,2,5)))
print(sum_of_evens_and_odd((2,4,6)))