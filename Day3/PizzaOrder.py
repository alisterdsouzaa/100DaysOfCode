# Pizza Shop.
# Based on user's order, work out their final bill.

print("Welcome to Pizaa Deliveries")

size = input("What size pizza do you want? S, M, or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1
else:
    bill = bill

print(f"Final bill for your pizza of size {size} is ${bill}")
