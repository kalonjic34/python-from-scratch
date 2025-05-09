"""
This script provides meal recommendations based on the ingredients provided.
It uses nested if-statements and logical operators to determine the output.
"""

ingredient1 = "Pasta"
ingredient2 = "Meatballs"
# ingredient2 = "Sausage"

if ingredient1 == "Pasta":
    if ingredient2 == "Meatballs":
        print("I recommend making pasta and meatballs")
    else:
        print("I recommend making plain pasta")
else:
    print("I have no recommendations")

if ingredient1 == "Pasta" and ingredient2 == "Meatballs":
    print("I recommend making pasta and meatballs")
elif ingredient1 == "Pasta":
    print("I recommend making plain pasta")
else:
    print("I have no recommendations")