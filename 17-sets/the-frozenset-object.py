mr_freeze = frozenset([1,2,3,2])
print(mr_freeze)

# mr_freeze.add(4) # AttributeError: 'frozenset' object has no attribute 'add'

regular_set = {1,2,3}
# print({regular_set: "Some value"})

print({mr_freeze : "Some value"})