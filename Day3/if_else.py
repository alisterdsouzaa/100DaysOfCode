# if else in Python
print("Welcome to the roller coaster!!")
height = int(input("Enter your height in cm.  "))

if height >= 120:
    print("Welcome to the ride")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Ticket price is 18$ for you")
    else:
        print("Ticket price is $7 for you")
else:
    print("Can't Ride. You have to grow taller for this ride")
