# *args
# N number of arguments using *agrs.


def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 4, 55, 6, 7))
