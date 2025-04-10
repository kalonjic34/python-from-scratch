class Guitar():
    def __init__(self):
        print(f"a new guitar is being being created! this object is {self}")

acoustic = Guitar()
electric = Guitar()

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)

# print(electric.year) #AttributeError: 'Guitar' object has no attribute 'year'
# print(acoustic.nickname) # AttributeError: 'Guitar' object has no attribute 'nickname'
