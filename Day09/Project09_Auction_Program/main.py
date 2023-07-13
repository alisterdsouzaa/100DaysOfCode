from replit import clear
from art import logo

print("Welcome to the Auction!!!")
print(logo)


bidders_dictionary = {}
flag = True

while flag:
    name = input("What is your name?")
    bid_amount = int(input("What is you bid amount?"))

    bidders_dictionary[name] = bid_amount
    print(bidders_dictionary)

    yes_no = input("Do you want to add another bidder?")
    if yes_no == "yes" or yes_no == "YES":
        flag = True
        clear()  # Clears the screen
    else:
        flag = False

max_bid = 0
max_bidder_name = ""
for bid in bidders_dictionary:
    value = bidders_dictionary[bid]
    if max_bid < value:
        max_bid = value
        max_bidder_name = bid

print(f"The maximum bid is {max_bid}. The name of the bidder is {max_bidder_name}")
