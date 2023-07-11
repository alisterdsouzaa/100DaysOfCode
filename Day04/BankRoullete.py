# Split the string method
import random

names_string = input("Give me everybody's name, separated by comma. ")
names = names_string.split(", ")

print(names)
num_of_people = len(names)
print(num_of_people)
num = random.randint(0,num_of_people-1)

print(names[num])
