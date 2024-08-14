''' Day 7: Hangman '''
''' I want to be a bit extra. '''
''' I want to use a big dictionary file to use words and have definitions for them. '''
''' Learning through playing. '''
import json
import os
import random
import sys 

# def debugger_is_active() -> bool:
#     """Return if the debugger is currently active"""
#     return hasattr(sys, 'gettrace') and sys.gettrace() is not None

def print_hidden_word(word, guessed_correct):
    word_mask = ''
    for char in word:
        if char in guessed_correct:
            word_mask += char
        else:
            word_mask += '_'
    return word_mask

# debugger_active = debugger_is_active()

# Opening JSON file
# if debugger_active:
#     json_file = open('100DaysofCoding\\Day 7\\dictionary.json')
# else:
#     json_file = open('Day 7\\dictionary.json')

# Opening JSON file
json_file = open('C:\\Users\\jon8z\\Documents\\Github\\100DaysOfCoding\\Day 7\\dictionary.json')

# returns JSON object as a dictionary
word_dictionary = json.load(json_file)

while True:
    guessed_letters = []
    guessed_correct = []
    word, definition = random.choice(list(word_dictionary.items()))
    word = word.lower()
    guesses_remaining = 5
    won = False

    while True:
        os.system('cls')
        print("Welcome to Hangman.")    
        print(f"Your word is: {print_hidden_word(word, guessed_correct)}")
        print(f"Your guessed letters are: {guessed_letters}")
        print(f"Remaining guesses are: {guesses_remaining}")
        guess = input("Please guess another letter: ").lower()
        if guess in guessed_letters:
            print("This letter has already been guessed. Try again.")
            continue

        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Character {guess} exists in the word.")
            guessed_correct.append(guess)
            if word == print_hidden_word(word, guessed_correct):
                print(f"You win. The word is: {word}.")
                print(f"Its definition is: {definition}")
                break
        else:
            print(f"Character {guess} does not exist in the word")
            guesses_remaining -= 1
            if guesses_remaining <= 0:
                print(f"You lose. The word was: {word}")
                print(f"Its definition is: {definition}")
                break
    
    play_again = input("Would you like to play again? (Y)/N: ")
    if play_again == 'n' or play_again == 'N':
        break

# Closing file
json_file.close()
