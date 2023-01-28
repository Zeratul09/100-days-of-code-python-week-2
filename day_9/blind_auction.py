import os
from art import logo, welcome_message
#HINT: You can call clear() to clear the output in the console.

#Introduce our user to the program:

print(welcome_message)
print(logo)


# Before we start our loop we will create 2 new varibles, an empty dict where we will write our key value pairs,
# # and a boolean to change when done with the game.
bidders = {}
IS_DONE = False

#While our varible is not true:
while not IS_DONE:

    #Ask for the bidder's name and bid:
    name = input("What is your name? ")
    bid = input("How much do you bid $? ")

    #Ask if there are any other bidders:
    response = input("Are there any other bidders? Type: 'Yes' or 'No' ")
    #Call our function:
    bidders[name] = bid

    #Check if we need to continue:
    if response.lower() == "yes":
        os.system('cls')
        #Testing code
        #print(bidders)
    else:
        IS_DONE = True
        max_value = max(bidders.values())
        max_key = max(bidders, key=bidders.get)
        print(f"The winner is {max_key} with a bid of {max_value}$!")


#pythontutor.com similar to Thonny