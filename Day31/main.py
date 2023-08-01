BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

import pandas
from tkinter import *
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    # print(data)  prints data frame
except FileNotFoundError:
    original_csv = pandas.read_csv("data/french_words.csv")
    to_learn = original_csv.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# print(to_learn)



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas Setup
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "bold"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Cross image / button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Right image / button
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
