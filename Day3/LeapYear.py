"""Leap years are years when an extra day is added to the end of the shortest month, February. 
This so-called intercalary day, February 29, is commonly referred to as leap day.
Leap years have 366 days instead of the usual 365 days and occur almost every four years."""

# Conditions for leap year.
"""
The year must be evenly divisible by 4.
If the year can also be evenly divided by 100, it is not a leap year;
unless...
The year is also evenly divisible by 400. Then it is a leap year.
"""

check_year = int(input("Enter your year to check. : "))

if check_year % 4 == 0:
    if check_year % 100 == 0 and check_year % 400 == 0:
        print("Leap Year.")
    else:
        print("Not a leap year.")
else:
    print("Not a leap year.")

