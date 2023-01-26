import turtle
import pandas
import time
import os.path
import threading


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'day25/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('day25/us-states-game-start/50_states.csv')
all_states = data.state.to_list()
guessed_states = []

s = turtle.Turtle()
s.penup()
s.hideturtle()
s.goto(-350, 250)
s.write("You have 5 Minutes to complete this challenge",
        font=("Arial", 15, "bold"))
# ----------------------------------------------------------------------------------
# TIMER
clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.goto(150, 250)


def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        clock.clear()
        clock.write(f'Time left: {timer}', font=("Arial", 25, "bold"))
        time.sleep(1)
        t -= 1


# def update_time(t, timer):
#     t.clear()
#     t.write(f'Time left: {timer}', font=("Arial", 25, "bold"))
#     t.clear()


countdown_time = 300  # time in seconds
start_time = time.time()  # starting time

# ----------------------------------------------------------------------------------
while len(guessed_states) < 50:

    # countdown timer
    remaining_time = countdown_time - int(time.time() - start_time)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(150, 250)
    mins, secs = divmod(remaining_time, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    t.clear()
    # update_time(t, timer)
    t.write(f'Time left: {timer}', font=("Arial", 25, "bold"))
    # time.sleep(1)

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # this if statement terminates the program when timer reaches zero and also saved missing states
    if remaining_time <= 0:
        if answer_state == 'Exit':
            update_time(t, timer)
            missing_states = [
                state for state in all_states if state not in guessed_states]
            # put data in a dictionary so we can access state title when we make list
            data_dict = {
                'state': missing_states
            }
            new_data = pandas.DataFrame(data_dict)
            new_data.to_csv("day25/us-states-game-start/states_to_learn.csv")
            break
        break
# when we exit, this will save all the remaining states in a new csv file
    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        # put data in a dictionary so we can access state title when we make list
        data_dict = {
            'state': missing_states
        }
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv("day25/us-states-game-start/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=('Arial', 12, 'bold'))


# ----------------------------------------------------------------------------------
# allows us to show the missing cities in red when we exit
missed_data = pandas.read_csv("day25/us-states-game-start/states_to_learn.csv")
missed_data_list = missed_data.state.to_list()
for state in missed_data_list:
    m_coordinates = data[data.state == state]
    m = turtle.Turtle()
    m.penup()
    m.hideturtle()
    m.color("red")
    m.goto(int(m_coordinates.x), int(m_coordinates.y))
    m.write(state, move=False, font=("Arial", 10, "bold"))


screen.mainloop()
