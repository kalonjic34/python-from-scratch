breakfasts = ["Eggs","Cereal", "Banana"]
lunches = ["Sushi","Chicken Teriyaki","Soup"]
dinners = ['Steak', "Meatballs", "Pasta"]

# print(zip(breakfasts,lunches,dinners))
# print(type(zip(breakfasts,lunches,dinners)))
# print(list(zip(breakfasts,lunches,dinners)))

for breakfast,lunches,dinners in zip(breakfasts,lunches,dinners):
    print(f"My meal for today was {breakfast} and {lunches} and {dinners}.")