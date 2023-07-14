# Calculator Project
from logo import logo


def add(num1, num2):
    """Returns addition of num1 and num2"""
    return num1 + num2


def sub(num1, num2):
    """Subtracts num2 from num1"""
    if num2 == 0:
        return "Cant divide by zero"
    return num1 / num2


def mult(num1, num2):
    """Returns multiplication of num1 * num2"""
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": divide
}


def claculator():
    print(logo)
    num1 = float(input("What is the first num? : "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats the next number? :"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue with {answer}, or type 'n' to start new calculation :") == "y":
            num1 = answer
        else:
            should_continue = False
            claculator()


claculator()
