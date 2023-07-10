# Tip Calculator Project

print("Welcome to the tip calculator \n")

total_bill = input(print("What was the total bill ? $ "))
total_bill = float(total_bill)

percentage_tip = int(input(print("What percentage of tip would you like to give? 10, 12 or 15. \n")))
percentage_tip = ((total_bill * percentage_tip) / 100)

numOfPeople = int(input(print("How many people you want to split the bill with? \n")))

total_bill_per_head = (total_bill + percentage_tip) / numOfPeople
total_bill_per_head = "{:.2f}".format(total_bill_per_head)

print(f"Your bill per person is ${total_bill_per_head}")
