# def calculate (n1, operator, n2):

from art import logo

print(logo)

def calculate(n1, operator, n2):

    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":  
        return n1 * n2
    elif operator == "/":  
        return n1 / n2

IS_DONE = False
first_iteration = True

while not IS_DONE:

    if first_iteration:
        n1 = float(input("What is n1? "))
    else:
        n1 = calculate(n1, operator, n2)
    operator = input("What operation do you wish to run? \n+\n-\n*\n/\n")
    n2 = float(input("What is n2? "))
    
    #print(calculate(n1, operator, n2))
    print(f"{n1} {operator} {n2} = {calculate(n1, operator, n2)}")

    response = input("Do you wish to make another a calculation? Type 'Yes or 'No' ")
    if response.lower() == "no":
        IS_DONE = True
        
    first_iteration = False