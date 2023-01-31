from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
RANDOM_INDEX = None
LIST_LENGTH = None

# -------------------- Create new flash cards ---------------------- #
try:
    words = pandas.read_csv("./Day_31/Flash_card_App/data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("./Day_31/Flash_card_App/data/french_words.csv")
finally:
    words_list = words.to_dict(orient="records")

def generate_new_word():
    global RANDOM_INDEX, LIST_LENGTH
    LIST_LENGTH = len(words_list)
    RANDOM_INDEX = random.randint(0, LIST_LENGTH - 1)
    word_in_french = words_list[RANDOM_INDEX]["French"]
    return word_in_french

def show_card_back():
    canvas.itemconfig(front_card, image=card_back)
    canvas.itemconfig(french, text="English", fill="white")
    canvas.itemconfig(text_in_french, text=f"{words_list[RANDOM_INDEX]['English']}", fill="white")
    right_button.config(state=NORMAL)
    wrong_button.config(state=NORMAL)

def show_card_front():
    right_button.config(state=DISABLED)
    wrong_button.config(state=DISABLED)
    canvas.itemconfig(french, text="French", fill="black")
    canvas.itemconfig(text_in_french, text=f"{generate_new_word()}", fill="black")
    canvas.itemconfig(front_card, image=card_front)
    window.after(3000, show_card_back)

# ------------------------- Save progress -------------------------- #
def update_list():
    show_card_front()
    del words_list[RANDOM_INDEX + 1]
    df = pandas.DataFrame(words_list)
    df.to_csv("./Day_31/Flash_card_App/data/words_to_learn.csv", index=False)

# --------------------------- UI Setup ----------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./Day_31/Flash_card_App/images/card_front.png")
card_back = PhotoImage(file="./Day_31/Flash_card_App/images/card_back.png")
front_card = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
french = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
text_in_french = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="./Day_31/Flash_card_App/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_card_front)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./Day_31/Flash_card_App/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=update_list)
right_button.grid(row=1, column=1)

show_card_front()

window.mainloop()