#Write your code below this line 👇

def prime_checker(number):

#Let's implement the facts of prime numbers from: https://www.factmonster.com/math-science/mathematics/prime-numbers-facts-examples-table-of-all-up-to-1000

#We will use a list to sum up our digits:
    digits = []
    for digit in str(number):
        digits.append(digit)
        #Testing code
        #print(digits)

#We will sum up our digits in the last for later conditional check:
    summed_digits = 0
    for digit in digits:
        summed_digits += int(digit)
        #Testing code
        #print(summed_digits)

#Now for the conditions to check:
                #Another solution is to use a for loop and use for digit in range(2, number).
    #If it's 0 or 1 it's not a prime number:
    if (number == 0) or (number == 1):
        print("It's not a prime number.")
    #If it's 2 or 3 or 5 then, it's a prime number:
    elif (number == 2) or (number == 3) or (number == 5):
        print("It's a prime number.")
    #If the sum of the digits can be divided by 3 with 0 remaining, then it's not a prime number:
    elif summed_digits % 3 == 0:
        print("It's not a prime number.")
    #If modulo 1 and modulo itself with 0 remaining is true, we will finally check if the number can be divided by 2, 3 or 5 with 0 remaining is true, if it is then it's not a prime number, otherwise it is:
    elif (number % 1 == 0) and (number % number == 0):
        if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0):
            print("It's not a prime number.")
        else:
            print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)