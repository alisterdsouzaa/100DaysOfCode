"""Body mass index (BMI) is a value derived from the mass (weight) and height of a person.
The BMI is defined as the body mass divided by the square of the body height, 
and is expressed in units of kg/m2, resulting from mass in kilograms and height in metres."""

# BMI = Weight / (Height)^2

print("This program will calculate your BMI \n")

# Accepting input from user for height ang weight
height = input(print("Please enter your height in meters : "))
weight = input(print("Please enter your weight in kg :"))

# typecasting string type to float
height = float(height)
weight = float(weight)

# Calculating BMI and storing as int in BMI variable
BMI = int(weight / (height ** 2))

print("Your BMI is " + str(BMI))
