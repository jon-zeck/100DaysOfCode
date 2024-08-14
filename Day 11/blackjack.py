''' Day 11: Blackjack project'''

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def hand_total(cards):
    total = 0
    for card in cards:
        total += card
    if 11 not in cards:
        return total
    elif total <= 21:
        return total
    else:
        # current total is above 21 and there is at least one Ace in the deck. Let's see if we can go lower than 21.
        for card in cards:
            if card == 11:
                card = 1
                total -= 10
                if total <= 21:
                    return total
    return total

def stand(player_total, comp_cards, deck):
    if player_total == 21:
        return True # blackjack, player wins
    while hand_total(comp_cards) < player_total:
        comp_cards.append(deck.pop())
    comp_total = hand_total(comp_cards)
    if comp_total <= 21 and comp_total >= player_total:
        return False # computer beat player score
    else:
        return True # computer lost (either over 21 or below player (although it cant score below player))

pot = 1000

while pot > 0:
    play = input("Do you want to play? (Y)/N: ")
    if play == "n" or play == "N":
        break

    deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    random.shuffle(deck)
    player_cards = []
    computer_cards = []

    player_cards.append(deck.pop())
    player_cards.append(deck.pop())
    computer_cards.append(deck.pop())
    computer_cards.append(deck.pop())

    while True:
        bet = float(input(f"how much do you want to bet, you have ${pot}: "))
        if bet > pot:
            print("You can't bet more than what you have.")
        else:
            break

    won = False
    while True:
        print(f"your cards are: {player_cards}. The total is {hand_total(player_cards)} ")
        print(f"computers cards are: [_, {computer_cards[1]}]. The total is {computer_cards[1]}")

        if hand_total(player_cards) == 21:
            won = True
            break

        hit_or_stand = input("Hit or Stand? (H)/S: ")
        if hit_or_stand == "S" or hit_or_stand == "s":
            won = stand(hand_total(player_cards), computer_cards, deck)
            break
        else:
            player_cards.append(deck.pop())
            if hand_total(player_cards) > 21:
                won = False
                break
    if won:
        print("You WON!")
        pot += bet * 2
    else:
        print("You LOST! Womp womp.")
        pot -= bet
    print(f"Your final hand: {player_cards} with a total of {hand_total(player_cards)}")
    print(f"Computer hand: {computer_cards} with a total of {hand_total(computer_cards)}")

print(f"You walk away with ${pot}.")

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.
