BACKGROUND_COLOR = "#B1DDC6"

import pandas
from tkinter import *
import random

data = pandas.read_csv("data/french_words.csv")
# print(data)  prints data frame

to_learn = data.to_dict(orient="records")
# print(to_learn)


def next_card():
    current_card = random.choice(to_learn)
    canvas.config()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "bold"))
canvas.create_text(400, 263, text="French word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Cross image / button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Right image / button
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

window.mainloop()

