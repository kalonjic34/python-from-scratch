         #012345678901234 
parrot = 'Norwegian Blue'

print(parrot)

print(parrot[0:6]) # Norweg
print(parrot[3:5]) # we
print(parrot[0:9]) # Norwegian
print(parrot[:9]) # Norwegian
print(parrot[10:]) # Blue

print(parrot[:6]) #Norweg
print(parrot[6:]) #ian Blue

print(parrot[:6]+parrot[6:]) #Norwegian Blue
print(parrot[:]) #Norwegian Blue


print(parrot[-14:-8]) #Norweg
print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val)for val in values])