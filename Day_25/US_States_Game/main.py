import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25/US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

""" def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() """

state_turtle = turtle.Turtle()
state_turtle.hideturtle()

data = pandas.read_csv("Day_25/US_States_Game/50_states.csv")
states = data["state"].to_list()

guessed_states = []
game_is_on = True
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    for state in states:
        if answer_state == state:
            guessed_states.append(answer_state)
            state_turtle.penup()
            state_turtle.goto(int(data.x[data.state == answer_state]), int(data.y[data.state == answer_state]))
            state_turtle.write(answer_state, align="center", font=("Courier", 10, "normal"))

states_to_learn = []
for state in states:
    if state not in guessed_states:
        states_to_learn.append(state)

states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("./Day_25/US_States_Game/states_to_learn.csv")