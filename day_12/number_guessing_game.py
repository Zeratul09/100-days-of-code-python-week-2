import random
import os
from art import logo

def difficulty_selector():
    '''
    This function decides the number of lives, based on the difficulty seleceted as input.

    Returns:
        int: The number of lives for the round.
    '''

    difficulty = ""

    while difficulty != "hard" or difficulty != "easy":
        difficulty = input("Select a difficulty! Type: 'hard' or 'easy': ").lower()
        if difficulty == "hard":
            return 5
        elif difficulty == "easy":
            return 10
        else:
            print("Invalid input. Please try again!")


def guessing_texts (actual_number, attempt):
    '''
    Prints a message based on the remaining number of lives when guessing.

    Parameters:
        actual_number (int): The random number that was selected.
        attempt (str): A string used which message will be printed.
    '''
    
    if attempt == "max_lives":
        print(f"JACKPOT! You've guessed it on your first try! The actual number was: {actual_number}. Well Played!")
        exit()
    if attempt == "still_have_lives":
        print(f"You've guessed it! The actual number was: {actual_number} Well Played!")
        exit()
    if attempt == "no_lives":
        print(f"You've ran out of lives. The actual number was: {actual_number}. Game over!")
        exit()


def checking_lives (lives):
    '''
    Checks if the number of lives is greater or equal to one and prints the appropiate message.

    Parameter:
        lives (int): The number of lives remaining.
    '''
    
    if lives > 1:
        print(f"Your current number of lives is: {lives}!")
    if lives == 1:
        print("This is your last life!")


def main():

    print (logo)
    answer = ""

    while answer != "y" or answer != "n":
        answer = input("Do you wish to play a game of 'Number Guessing'? Type: 'y' or 'n' ").lower()
        if answer == "y":
            print('''
            The rules are the following: A random number will be selected from 1 - 100
            (inclusive) and you need to guess the correct number. You will be given hints
            when you either guessed too high or too low compared to the random number. 
            You may select from 2 difficulties: 'Easy Mode' in which you have 10 lives 
            to guess and 'Hard Mode' in which you have 5 lives to guess. Good luck!
            ''')
            break
        elif answer == "n":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please try again!")
    
    starting_lives = difficulty_selector()
    lives = starting_lives
    actual_number = random.randint(1, 100)

    os.system('cls')
    print("I am thinking a number between 1-100 (inclusive), go ahead and guess it :)!")

    end_of_game = False
    while lives != 0 or not end_of_game:
        
        checking_lives(lives)
        
        player_guess = int(input("Guess a number from 1 - 100 (inclusive): "))
        print(f"You've guessed: {player_guess}")
        if player_guess == actual_number:
            end_of_game = True
            if lives == starting_lives:
                print(guessing_texts(actual_number, "max_lives"))
            else:
                print(guessing_texts(actual_number, "still_have_lives"))
        elif player_guess > actual_number:
            lives -= 1
            if lives == 0:
                print(guessing_texts(actual_number, "no_lives"))
            print("You've guessed too high. Try again!")
        elif player_guess < actual_number:
            lives -= 1
            if lives == 0:
                print(guessing_texts(actual_number, "no_lives"))
            print("You've guessed too low. Try again!")

main()