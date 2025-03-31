# Define a sum_of_lengths function that accepts a list of strings
# The function should return the sum of the string lengths

def sum_of_lengths(words):
    total = 0
    for word in words:
        total += len(word)
    return total
print(sum_of_lengths(["hello","Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense","or","confidence"]))

# Define a product function that accepts a list of numbers
# The function should return the product of the numbers
# The list will always have at least one value

def product(numbers):
    total_product = 1
    for number in numbers:
        total_product *= number
    return total_product
print(product([1,2,3]))      
print(product([4,5,6,7]))      
print(product([10]))      