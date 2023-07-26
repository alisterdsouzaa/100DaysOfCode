import pandas as pd

read_data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(read_data)
# new_dict = pd.DataFrame.to_dict(read_data)
# print(new_dict)

# Create dictionary from csv data
new_dict = {row.letter: row.code for (index, row) in read_data.iterrows()}
print(new_dict)

# take user input and give a list of NATO words to the user back.
user_input = input("Enter your word :").upper()
print(user_input)

user_list = [new_dict[letter] for letter in user_input]
print(user_list)

