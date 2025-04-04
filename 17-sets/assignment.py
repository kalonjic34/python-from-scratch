# Declare a set with 3 of your favorite movies as strings.
# Assign it to a movies variable.
movies  = {"Inception","American Gangster", "Heat"}
print(movies)

# Declare a set with the first four months of the year as strings.
# Assign it to a months variable.
months = {"January", "February", "March", "April"}
print(months)

# Create an empty list and assign it to an empty variable.
empty = {}

# Define a remove_duplicates function that accepts a single list as an argument.
# The function should return a list with all of the duplicates from the original list removed.
# The order of elements in the returned list is irrelevant.

def remove_duplicates(elements):
    return list(set(elements))

print(remove_duplicates([1,2,2,1]))
print(remove_duplicates([1,2,3,4]))