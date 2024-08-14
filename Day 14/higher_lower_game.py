from game_art import LOGO, LOGO_VS
from game_data import DATA
import os
import random

def print_higher_lower(data_obj_1, data_obj_2):
    os.system('cls')
    print(LOGO)
    print(f"COMPARE: {data_obj_1['name']}")
    print(LOGO_VS)
    print(f"{data_obj_2['name']}")

def select_objects(winning_obj):
    if winning_obj == {}:
        obj_one = random.choice(DATA)
    else:
        obj_one = winning_obj
    while True: # choose a unique object for choice two.
        obj_two = random.choice(DATA)
        if not obj_one['name'] == obj_two['name']:
            break
    return obj_one, obj_two

def user_choice_input():
    while True: # make sure the user chooses one of the objects as their answer.
        user_choice = {}
        user_choice_name = input("Who do you think has more instagram followers: ").lower()
        if user_choice_name == choice_one['name'].lower():
            user_choice = choice_one
            other_choice = choice_two
            break
        elif user_choice_name == choice_two['name'].lower():
            user_choice = choice_two
            other_choice = choice_one
            break
        print("You did not choose a valid name. Try again.")
    return user_choice, other_choice

def print_followers(user_choice, other_choice):
    return f"{user_choice['name']} has {user_choice['follower_count']}m followers and {other_choice['name']} has {other_choice['follower_count']}m followers"

if __name__ == "__main__":
    while True:
        winning_obj = {}
        points = 0
        while True:
            choice_one, choice_two = select_objects(winning_obj)
            print_higher_lower(choice_one, choice_two)
            user_choice, other_choice = user_choice_input()
            if user_choice['follower_count'] >= other_choice['follower_count']:
                winning_obj = user_choice
                points += 1
                print(f"Correct! {print_followers(user_choice, other_choice)}")
                input(f"Current Score: {points}")
            else:
                winning_obj = other_choice
                print(f"Wrong! {print_followers(user_choice, other_choice)}")
                print(f"Your final tally is: {points}")
                break
        keep_playing = input("Do you want to play again? (Y)/N: ")
        if keep_playing.lower() == 'n':
            break

''' There is a key difference between my implementation and Angela Yu's.
    In mine, the correct guess is kept as the comparison for the player.
    The issue is that eventually it will become Instagram as it has the most followers.
    In Angela's implementation, choice B becomes choice A for the new round.
    That keeps the game fresh and interesting.
    I could fix this, but the change is trivial and I'm not going to play this again. '''