import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")

image_path = "Udemy/Day25/us-states-game-start/blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

data = pandas.read_csv("Udemy/Day25/us-states-game-start/50_states.csv")
state_list = data["state"].to_list()

correct = 0
guessed = []

for n in range(0, 50):
    answer_state = screen.textinput(
        title=f"{correct}/50 Guess the state.", prompt="What's the other states name?"
    )

    guessed.append(answer_state.title())

    if answer_state.title() in state_list:
        correct += 1
        # show the statw
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.state == answer_state]
        x_cor = int(answer_data.x)
        y_cor = int(answer_data.y)
        t.goto(x=x_cor, y=y_cor)
        t.write(answer_state)

    if answer_state.lower() == "exit":
        break

missed_list = []
for state in state_list:
    if state not in guessed:
        missed_list.append(state)

    missed_data = pandas.DataFrame(missed_list)
    missed_data.to_csv("Udemy/Day25/us-states-game-start/state_missed.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# screen.exitonclick()
