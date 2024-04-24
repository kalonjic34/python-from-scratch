friend = "James"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello friend!")
else:
    print("Hello stranger!")

print(bool(5))
print(bool(0))

if 4:
    print("Runs")

name = input("Enter your name: ")
if name:
    print("We know your name")


friends = ["James", "Ian", "Sam"]
family = ["Ash","Will"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello friend")

elif user_name in family:
    print("Hello family")
else:
    print("We dont know you")