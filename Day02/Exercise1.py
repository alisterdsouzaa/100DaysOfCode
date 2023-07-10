# Write a program that adds the digit in a 2-digit number.
# if the i/p was 35 then the output should be 3 + 5 = 8

num = (input("Enter your two digit number!! \n : "))
print(num)
print("\n")

print(type(num))

num1 = int(num[0])
num2 = int(num[1])

result = num1 + num2
print(result)
