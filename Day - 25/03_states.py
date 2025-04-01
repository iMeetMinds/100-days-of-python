import turtle
import pandas
from turtle_state import StatePrint

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
state_list = states_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state name?").title()

    if user_answer == 'Exit':
        break

    if (user_answer in state_list) and (not user_answer in guessed_state):
        state_det = states_data[states_data.state == user_answer]
        x_cor = int(state_det.x.iloc[0])
        y_cor = int(state_det.y.iloc[0])
        tim = StatePrint(x_cor, y_cor, state_det.state.item())
        guessed_state.append(state_det.state.item())

remaining_states = [n for n in state_list if not n in guessed_state]

new_data = pandas.DataFrame(remaining_states)
new_data.to_csv('states_to_learn.csv')