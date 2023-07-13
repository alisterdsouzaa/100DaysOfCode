"""
You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)

And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year
has 29 days in February."""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(input_year, input_month):
    if 12 > input_month < 1:
        return print("Invalid Month")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    flag = is_leap(input_year)
    if flag:
        month_days[input_month-1] = 29
    return month_days[input_month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)