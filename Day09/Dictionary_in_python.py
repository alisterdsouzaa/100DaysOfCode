programming_dictionary = {
    "bug": "An error in programming when a program does not function as expected",
    "function": "A piece of code you can call over and over again.",
    "Loop": "If you want to perform iteration."
}

print(programming_dictionary["function"])
programming_dictionary[1] = "One"  # Adding key : value in dictionary

# Creating an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#  wiping an existing dictionary
#programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary ["Bug"] = " Hi Bug"
print(programming_dictionary["Bug"])

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

