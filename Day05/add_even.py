#  Sum of all the even numbers 1 -100
even_total = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_total += num

print(even_total)