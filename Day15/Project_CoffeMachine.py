MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    print("Please insert coins!")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickels = int(input("How many quarters?: "))
    pennies = int(input("How many quarters?: "))
    total = float((0.25 * quarters) + (dimes * 0.10) + (nickels * 0.05) + (0.01 * pennies))
    return total


def get_cost(coffee_choice, total):
    """Calculates the total bill of coffee"""
    money_required = MENU[coffee_choice]
    get_cost = money_required['cost']
    print(get_cost)
    if get_cost > total:
        print("Not sufficient money.")
        print(f"Required amount is {get_cost}")
    elif total > get_cost:
        print("Transaction Successful.")
        print(f"Here is your change of {total - get_cost}$")
    else:
        print("Transaction Successful.")


def resources_required(coffe_choice):
    menu = MENU[coffe_choice]


is_on = True

while is_on:
    coffee_choice = input("What would you like to have? (espresso/latte/cappuccino) : ")
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Water : {resources['coffee']}ml")
        print(f"Money {profit}$")
    # total = insert_coins()

    # get_cost(coffee_choice,total)
    resources_required(coffee_choice)
