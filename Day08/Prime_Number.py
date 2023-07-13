# Prime number checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is Not a Prime Number")


number = int(input("Enter number to check : "))
prime_checker(number)
