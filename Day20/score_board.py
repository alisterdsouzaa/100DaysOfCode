from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 10, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", move=False, align="center", font=('Arial', 20, 'bold'))
