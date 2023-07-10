# if else in Python
print("Welcome to the roller coaster!!")
height = int(input("Enter your height in cm.  "))

bill = 0

if height >= 120:
    print("Welcome to the ride")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 18
        print("Ticket price is 18$ for you")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Ticket price is $7 for you")
        bill = 7

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        # Add $3 to their bill.
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("Can't Ride. You have to grow taller for this ride")
