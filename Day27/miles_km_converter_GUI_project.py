from tkinter import *

MILE = 1.6

window = Tk()
window.minsize(width=200, height=200)
window.title("Miles to Kilometers converter")
window.config(padx=20, pady=20)


def mile_to_km():
    miles = float(miles_input.get())
    result = int(miles * MILE)
    label_result.config(text=result)


miles_input = Entry()
miles_input.grid(column=1, row=0)

label_miles = Label(text="Miles", font=('Arial', 10, 'bold'))
label_miles.grid(column=3, row=0)

label_km = Label(text="Kilometers", font=('Arial', 10, 'bold'))
label_km.grid(column=3, row=1)

label_isEqualTo = Label(text="is equal to ", font=('Arial', 10, 'bold'))
label_isEqualTo.grid(column=0, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

window.mainloop()
