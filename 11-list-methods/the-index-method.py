pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))

# print(pizzas.index("Olive"))
# ValueError: 'Olive' is not in list

if "Olives" in pizzas:
    print(pizzas.index("Olives"))
    
print(pizzas.index("Pepperoni", 2))
print(pizzas.index("Sausage", 3))
print(pizzas.index("Sausage", 2))
