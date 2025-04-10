class Guitar():
    def __init__(self,wood):
        self.wood = wood

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)

baritone = Guitar("Alder")

print(baritone.wood)

print(acoustic) # <__main__.Guitar object at 0x000001C6FF7469C0>
print(baritone) # <__main__.Guitar object at 0x000001C6FF746A80>