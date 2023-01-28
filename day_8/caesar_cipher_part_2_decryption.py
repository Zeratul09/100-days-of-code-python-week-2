alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    #We create a new empty varible:
    cipher_text = ""
    #For each letter in the plain_text do the following
    for letter in plain_text:
        #Get the position of the letter in our alphabet list.
        position = alphabet.index(letter)
        #Add the shift amount to the position and put it into the new_position variable.
        new_position = position + shift_amount
        #Starting adding together the letters to our empty string:
        cipher_text += alphabet[new_position]
    #Finally, print our ciphered text:
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cipher_text, shift_amount):
    #We create a new empty varible:
    deciphered_text = ""
    #For each letter in the ciphered_text do the following
    for letter in cipher_text:
        #Get the position of the letter in our alphabet list.
        position = alphabet.index(letter)
        #Deduct the shift amount to the position and put it into the new_position variable.
        old_position = position - shift_amount
        #Starting adding together the letters to our empty string:
        deciphered_text += alphabet[old_position]
    #Finally, print our deciphered text:
    print(f"The decoded text is {deciphered_text}")


  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

#If we write either "encode" or "decode" do the following:
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)