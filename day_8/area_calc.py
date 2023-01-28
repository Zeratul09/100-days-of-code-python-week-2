#We import our required modules:
import math

#Write your code below this line 👇
#We define our function in a way so that the function calling at the bottom works:
def paint_calc(height, width, cover):

#We calculate the answer
#You may split the area and cans of paint calculation into two, but it's not necessary unless we would really want to use the area varible:
    answer = (height * width) / cover
#We round it up to the nearest whole number (math.ceil (ceiling, rounding up, math.floor (floor, rounding down)))
    rounded_up = math.ceil(answer)
#Finally, we will print out the result
    print(f"You'll need {rounded_up} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)