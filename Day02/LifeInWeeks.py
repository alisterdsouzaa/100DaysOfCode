# Calculating total Life remaining years, days, months and in weeks
# 1 Year = 12 Months, 52 Weeks, & 365 Days.

print("Enter your age : ")
age = int(input())

# Calculate num of years remaining.

# Assuming life span of 100 and calculating num of years remaining, days and weeks remaining.
years_remaining = 100 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (
    f"You have {years_remaining} Years , {months_remaining} Months, {weeks_remaining} Weeks, {days_remaining} Days "
    f"remaining in your life.")

print(message)

# End of file
