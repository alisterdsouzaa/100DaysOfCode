import pandas
import turtle


screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data["state"].to_list()
# print(data_list)

guessed_states = []

while len(guessed_states) < 50:
    ans_state = screen.textinput(title=f"State's Correct {len(guessed_states)}/50", prompt="What another state's name? ")
    guess_answer_in_title_case = ans_state.title()
    # print(guess_answer_in_title_case)

    if guess_answer_in_title_case == "Exit":
        missing_states = []
        for states in data_list:
            if states not in guessed_states:
                missing_states.append(states)
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("States_to_learn.csv")
        break

    if guess_answer_in_title_case in data_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_answer_in_title_case]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess_answer_in_title_case)
