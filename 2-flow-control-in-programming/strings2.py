number = input("Pease enter a series of number, suing any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric(): 
        separators = separators +char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val)for val in values]))