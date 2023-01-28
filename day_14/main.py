from art import logo
from art import vs
from game_data import data
import random

#Selecting 2 items from the list randomly. (Keep in mind we have a dictionaries as part of a list)

def main():

    number_of_items = len(data)

    choice_1 = data[random.randint(0, number_of_items-1)]

    has_lost = False
    score = 0

    while not has_lost:

        choice_2 = data[random.randint(0, number_of_items-1)]

        print (f"Your current score is: {score}!")
        print(f"Does {choice_2['name']} has more or less followers than {choice_1['name']}?")

        follower_1 = choice_1['follower_count']
        print(f"{choice_1['name']} has {choice_1['follower_count']} followers and here are a few extra hints: ")
        print("Description: " + choice_1['description'] + '\n'"Country: " + choice_1['country'])

        print(vs)

        follower_2 = choice_2['follower_count']
        print(f"Here are some extra hints about {choice_2['name']}:")
        print("Description: " + choice_2['description'] + '\n'"Country: " + choice_2['country'])


        answer = input(f"\nType either 'A' or 'B' for your choice! ").lower()

        if choice_1["follower_count"] >= choice_2["follower_count"]:
            if answer == 'a':
                score += 1
                print("You were correct, onto the next round")
            elif answer == 'b':
                has_lost = True
                print(f"You've lost! {choice_2['name']} has more followers.")
                print(f"Your final score is: {score}!")
            else:
                print("Incorrect input, try again!")
        elif choice_1["follower_count"] <= choice_2["follower_count"]:
            if answer == 'a':
                has_lost = True
                print(f"You've lost! {choice_2['name']} has more followers.")
                print(f"Your final score is: {score}!")
            elif answer == 'b':
                score += 1
                choice_1 = choice_2
                print("You were correct, onto the next round")

main()