import turtle
import pandas
import time
import os.path


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'day25/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

start = time.time()

data = pandas.read_csv('day25/us-states-game-start/50_states.csv')
all_states = data.state.to_list()
guessed_states = []

# ----------------------------------------------------------------------------------
# TIMER
clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.goto(150, 250)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        clock.clear()
        clock.write(f'Time left: {timer}', font=("Arial", 25, "bold"))
        time.sleep(1)
        t -= 1


countdown(300)
# ----------------------------------------------------------------------------------
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day25/us-states-game-start/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# ----------------------------------------------------------------------------------
# allows us to show the missing cities in red when we exit
missed_data = pandas.read_csv("day25/us-states-game-start/states_to_learn.csv")
missed_data_list = missed_data
for state in missed_data_list:
    m_coordinates = data[data.state == state]
    m = turtle.Turtle()
    m.penup()
    m.hideturtle()
    m.color("red")
    m.goto(int(m_coordinates.x), int(m_coordinates.y))
    m.write(state, move=False, font=("Arial", 10, "normal"))


screen.mainloop()
