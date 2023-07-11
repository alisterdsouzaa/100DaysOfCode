"""
Make a rock, paper, scissors game.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.

"""
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_rps = [rock, paper, scissors]  # List of variables.

print(f"You choose : {list_rps[user_choice]}\nand Computer choose {list_rps[computer_choice]} ")

print("#-------------------------------------------------------------------------------------------#")

if user_choice == 0 and computer_choice == 1:
    print(paper)
    print("Computer wins.")
elif user_choice == 1 and computer_choice == 2:
    print(scissors)
    print("Computer wins.")
elif user_choice == 2 and computer_choice == 0:
    print(rock)
    print("Computer wins")
elif user_choice == 0 and computer_choice == 2:
    print(rock)
    print("You won")
elif user_choice == 1 and computer_choice == 0:
    print(paper)
    print("You won")
elif user_choice == 2 and computer_choice == 1:
    print(scissors)
    print("You won.")
else:
    print(list_rps[user_choice])
    print("It's a Draw")
