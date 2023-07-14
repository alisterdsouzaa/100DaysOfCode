#  Black Jack Game. / 21 Game
import random
from logo import logo

print(logo)
print("Welcome to BlackJAck / 21\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_cards = []
computer_cards = []


def calculate_score(individual_list_of_cards):
    score = 0
    for card_value in individual_list_of_cards:
        score += card_value
    return score


continue_play = True

while continue_play:
    for i in range(0, 2):
        random_choice = random.choice(cards)
        user_cards.append(random_choice)

        random_choice = random.choice(cards)
        computer_cards.append(random_choice)

    result1 = calculate_score(user_cards)
    print(f"Your cards are : {user_cards[0]} and {user_cards[1]}. And your score is {result1}")

    result2 = calculate_score(computer_cards)
    print(f"Computers cards are : {computer_cards[0]} and '__'.\n\n")

    play_more = input("Do you want to add one more card to your cards? If yes type 'y' else type 'n' : ")
    if play_more == "y":
        for i in range(0, 1):
            random_choice = random.choice(cards)
            user_cards.append(random_choice)
            result1 += user_cards[2]

    if result1 >= 21:
        print("You Loose.")
        print(f"Your final score was {result1}")

    elif result1 < 21 and result1 > result2:
        print(f" You won. Your total score is {result1} ")
        print(f"Computer total score was {result2} and Computer cards were {computer_cards}.")

    elif result2 > result1:
        print(f"You Loose. Computer score is {result2} and Your score is {result1}")

    elif result1 == result2:
        print(f"Your score and computers score is {result1} and {result2}")
        print("DRAW")

    wanna_play = input("\nDo you want to play more black jack again???. if Yes type 'y' else type 'n' : ")
    if wanna_play == "y":
        continue_play = True
        user_cards = []
        computer_cards = []
    else:
        continue_play = False
        print("Exiting Game.")
