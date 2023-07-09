# Write a program that works out whether if a given number is an odd or even
# Even numbers can be divided by 2 with no remainder

number = int(input("Enter your number to check whether Even or Odd : "))

if number % 2 == 0:
    print(f"Entered number {number} is Even.")
else:
    print(f"Entered number {number} is Odd")

