from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window["padx"] = 20
window["pady"] = 20

mylabel = Label(text="I am label", font=('Arial', 20, 'bold'))
mylabel.grid(column=0, row=0)
mylabel.config(padx=50, pady=50)
# mylabel.pack()

def button_fun():
    print("I am button")
    mylabel["text"] = "I am updated label"

button = Button(text="Click me", command=button_fun)
# button.grid(column=3, row=0)
button.grid(column=2, row=0)
# button.pack()

input = Entry()
input.grid(column=3, row=2)
# input.pack()

window.mainloop()