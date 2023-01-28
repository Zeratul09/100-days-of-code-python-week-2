alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#if not direction == "encode" or not direction == "decode":
#    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#We will combine the 2 functions by adding the 3rd variable called direction (argument) to the action (parameter).
def caesar(text, shift_amount=shift, action=direction):

    #Another way of solving this (by the tutor of the course, Angela) is to simply combine the 2 old functions into one and not run it as 2 separate things.
    #We will check the action if it's "encode" we will run the old encrypt() function and add our varibles from the inputs the following way:
    if action == "encode":
        plain_text = text
        shift_amount = shift
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")

    #We will check the action if it's "decode" we will run the old decrypt() function and add our varibles from the inputs the following way:
    elif action == "decode":
        cipher_text = text
        shift_amount = shift
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift_amount=shift, action=direction)