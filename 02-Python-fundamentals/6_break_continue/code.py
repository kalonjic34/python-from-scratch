car = ["ok", "ok","ok","faulty","ok","ok"]

for status in car:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to the customer!")


for status in car:
    if status == "faulty":
        print("Found faulty car, skipping..")
        continue
    print(f"This car is {status}")
    print("Shipping new car to the customer!")