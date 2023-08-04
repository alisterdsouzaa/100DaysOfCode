from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __int__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.grid()

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Q text", fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2)


        self.window.mainloop()