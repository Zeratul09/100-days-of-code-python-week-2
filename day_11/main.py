############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
from art import logo

def compare_scores(player_cards, dealer_cards):
    '''
    This function takes the player_cards and dealer_cards as parameters and compares them to one another.
    '''

    if sum(player_cards) > sum(dealer_cards):
        game_ending_message(player_cards, dealer_cards, "player")
    elif sum(player_cards) == sum(dealer_cards):
        game_ending_message(player_cards, dealer_cards, "draw")
    else:
        game_ending_message(player_cards, dealer_cards, "house")


def over_21(cards):
    '''
    This function takes "cards" as a parameter checks any player's cards if they went over 21 or not:
    '''

    if sum(cards) > 21 :
        return True
    else:
        return False
    

def game_ending_message(player_cards, dealer_cards, result):
    '''
    This function takes 3 parameters: player_cards, dealer_cards, result, it compares the scores and will print a message when the function is called.
    '''

    message_ending = (f"Your cards were {player_cards} the house's cards were {dealer_cards}!")

    if result == "draw":
        print(f"It's draw! {message_ending}")
    elif result == "player":
        print(f"You've won! {message_ending}")
    elif result == "house":
        print(f"You've lost! {message_ending}")

def play_game():
    '''
    This function will start our game if at the end of the function we type "y".
    '''

    print (logo)   

    #Declare our list of cards:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #Declare our varibles: player_cards [list], dealer_cards [list], is_the_game_over (boolean)

    player_cards = []
    dealer_cards = []
    is_the_game_over = False
    dealer_drew_card = False

    #Get beginning cards:
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))


    #Print out your card and the house's first card
    print(f"Your first card is {player_cards[0]}")
    print(f"The house's first card is {dealer_cards[0]} ")

    #Picking random numbers(cards)
    while not is_the_game_over:
        
    
        #Getting input
        pick_a_card = input("Do you wish to pick another card? Yes/No ")

        if pick_a_card.lower() == "yes":
            player_cards.append(random.choice(cards))
            if 11 in player_cards and sum(player_cards) > 21:
                for i in range(len(player_cards)):
                    if player_cards[i] == 11:
                        player_cards[i] = 1
            if not dealer_drew_card:
                dealer_cards.append(random.choice(cards))
                dealer_drew_card = not dealer_drew_card
        else:
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.choice(cards))
                if 11 in dealer_cards and sum(dealer_cards) > 21:
                    for i in range(len(dealer_cards)):
                        if dealer_cards[i] == 11:
                            dealer_cards[i] = 1
                if sum(dealer_cards) > 21:      
                    game_ending_message(player_cards, dealer_cards, "player")
                    quit()

            is_the_game_over = True
            compare_scores(player_cards, dealer_cards)

        print(player_cards)
        if over_21(player_cards) and over_21(dealer_cards):
            game_ending_message(player_cards, dealer_cards, "draw")
            quit()
        elif over_21(player_cards):
            game_ending_message(player_cards, dealer_cards, "house")
            quit()
        elif over_21(dealer_cards):
            game_ending_message(player_cards, dealer_cards, "player")
            quit()
        
while input("Do you wish to play BlackjacK? Type 'y' or 'no ") == "y":
    os.system('cls')
    play_game()



##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

