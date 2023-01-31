# from tkinter import *

# def miles_to_km():
#     miles = float(input.get())
#     result = miles * 1.609344
#     result_label.config(text= f"{round(result, 2)}")

# window = Tk()
# window.title("Mile to Km Converter")
# window.minsize(width=300, height=150)
# window.config(padx=50, pady=50)

# #Equal to label
# equal_to_label = Label(text="is equal to", font=("Arial", 14, "normal"))
# equal_to_label.grid(column=0, row=1)

# #Miles label
# miles_label = Label(text="Miles", font=("Arial", 14, "normal"))
# miles_label.grid(column=2, row=0)

# #Km label
# km_label = Label(text="Km", font=("Arial", 14, "normal"))
# km_label.grid(column=2, row=1)

# #result label
# result_label = Label(text="0", font=("Arial", 14, "normal"))
# result_label.grid(column=1, row=1)

# #Entry
# input = Entry(width=10)
# input.grid(column=1, row=0)

# #Button
# button = Button(text="Calculate", command=miles_to_km)
# button.grid(column=1, row=2)

# window.mainloop()

# Udemy solution
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{round(km, 2)}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column="1", row="0")

miles_label = Label(text="Miles")
miles_label.grid(column="2", row="0")

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column="0", row="1")

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column="1", row="1")

kilometer_label = Label(text="Km")
kilometer_label.grid(column="2", row="1")

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column="1", row="2")

window.mainloop()