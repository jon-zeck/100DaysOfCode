''' Day 4: Rock Paper Sissors --- Beginner '''
import random
RPS_dict = {"Rock": 0, "Paper": 1, "Scissors": 2}
RPS = ["Rock", "Paper", "Scissors"]

won = False
while True:
    choice = input("Rock, Paper or Scissors: ")
    if not choice == "Rock" and not choice == "Paper" and not choice == "Scissors":
        print("Invalid Input, try again.")
        continue
    
    choice_int = RPS_dict[choice]
    computer_choice = random.randint(0, 2)
    outcome = computer_choice - choice_int
    if outcome == 0: # both chose the same object
        print(f"You chose: {choice}. Computer chose: {RPS[computer_choice]}. Draw.")
    elif outcome == -1 and computer_choice == 0: # computer picks rock, user picks paper
        won = True
        break
    elif outcome == -2: # computer picks rock, user picks scissors
        won == False
        break
    elif outcome == -1 and computer_choice == 1: # computer picks paper, user picks scissors
        won = True
        break
    elif outcome == 1 and computer_choice == 1: # computer picks paper, user picks rock
        won = False
        break
    elif outcome == 2: # computer picks scissors, user picks rock
        won = True
        break
    elif outcome == 1 and computer_choice == 2: # computer picks scissors, user picks paper
        won = False
        break

if won:
    print(f"You chose: {choice}. Computer chose: {RPS[computer_choice]}. You win.")
else:
    print(f"You chose: {choice}. Computer chose: {RPS[computer_choice]}. Computer wins.")

''' I did think my implimentation couldve been done better and I was correct:
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
'''