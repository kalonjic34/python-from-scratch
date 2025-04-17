class Nonsense():
    def __init__(self):
        self.__some_attribute = "hello"
        
    def __some_method(self):
        print("This is coming from some_method")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

# print(n.__some_attribute)
# print(n.some_method_attribute)
# print(sn.__some_method_attribute)
# print(sn.some_method_attribute)

# sn.__some_method()

print(n._Nonsense__some_attribute)
print(sn._Nonsense__some_attribute)
print(n._Nonsense__some_method())
print(sn._Nonsense__some_method())