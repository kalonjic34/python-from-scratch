flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices(["Seattle"])) #TypeError: 'dict' object is not callable
# print(flight_prices["chicago"]) # KeyError: 'chicago'

gym_membership_packages = {
    29: ["Machine"],
    49: ["Machine", "Vitamins Supplements"],
    79: ["Machine", "Vitamins Supplements","Sauna"]
}

print(gym_membership_packages[49])
print(gym_membership_packages[79])

print(gym_membership_packages.get(29, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100))
