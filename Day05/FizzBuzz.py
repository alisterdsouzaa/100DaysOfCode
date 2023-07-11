"""
Fizz buzz is a group word game for children to teach them about division.
Players take turns to count incrementally, replacing any number divisible by three with the word "fizz"
, and any number divisible by five with the word "buzz",
and any number divisible by both 3 and 5 with the word "fizzbuzz".

"""
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
