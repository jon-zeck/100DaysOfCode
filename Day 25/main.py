''' Aim of 'today' is to recreate the sporcle's 'name all 50 US states' game '''
from turtle import Turtle, Screen
import os, pandas as pd
from country import Country

def find_path(name):
    cwd = os.getcwd()
    for root, _, files in os.walk(cwd):
        if name in files:
            return os.path.join(root, name)

if __name__ == '__main__':
    screen = Screen()
    screen.title("US States Quiz")
    
    try:
        img_name = "blank_states_img.gif"
        image_path = find_path(img_name)
    except:
        print("Failed to find the image")

    try:
        csv_name = "50_states.csv"
        states_csv_path = find_path(csv_name)
    except:
        print("Failed to find the 50 states csv")
    
    screen.addshape(image_path)
    turtle = Turtle()
    turtle.shape(image_path)

    states_data = pd.read_csv(states_csv_path)
    states_list = states_data.state.to_list()

    number_of_states = 50
    while states_list:
        answer_state = screen.textinput(f"You have {number_of_states - len(states_list)}/{number_of_states} correct", "Name another state:")
        if answer_state.lower() == "exit" or answer_state.lower() == "quit":
            break
        state_info = states_data[states_data.state == answer_state]
        if state_info.empty:
            continue
        if not answer_state in states_list:
            continue
        Country(state_info)
        states_list.remove(answer_state)
    
    input(f"End of game. You got {number_of_states - len(states_list)}/{number_of_states} correct")
