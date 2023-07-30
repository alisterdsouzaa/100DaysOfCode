from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator .
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(message="Do not leave any field's empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered :\nWebsite :{website}\n"
                                                              f"Email : {email}\nPassword: {password}\n")

        # message box module
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager/Generator")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas()
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Label and Entries
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=0, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=0, row=2, columnspan=2)
email_entry.insert(0, "alisterdsouzaa@outlook.com")

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

add_button = Button(text="Add", width=36, bg="yellow", command=save_data)
add_button.grid(row=4, column=0, columnspan=2)

button = Button(text="Generate Password : ", command=generate_password)
button.grid(column=2, row=3)

window.mainloop()
