"""
This script demonstrates the use of escape characters in Python
It includes examples of newline, tab, quotes, backslashes, raw strings, 
and multi-line statements
"""
print("This will \nbegin on a \nnew line")

print("\tOnce upon a time")

# print(""To be or not to be", said Hamlet") 
# SyntaxError: invalid syntax.

print("\"To be or not to be\", said Hamlet") 
print('\'To be or not to be\', said Hamlet') 

print("Let's print a backlash: \\")

file_name = r"C:\\news\travel"
print(file_name)

some_random_number = 5
some_obscure_calculation = 25
some_additional_statistic_fetched_from_somewhere = 10

final = some_random_number + \
        some_obscure_calculation + \
        some_additional_statistic_fetched_from_somewhere
        
print(some_random_number,
    some_obscure_calculation,
    some_additional_statistic_fetched_from_somewhere)