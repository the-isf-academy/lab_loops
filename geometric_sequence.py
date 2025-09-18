# geometric_sequence.py

from turtle import *

# 💻 Translate the Pseudocode into Python Code  💻 #


# store the starting number, 1, in a variable called num 
# ask the user what the ratio should be and store it in a variable called ratio 
# loop 10 times 
    # print num
    # update the value of num to num * ratio 

num = 1
ratio = int(input("What should the ratio of the sequence be? "))

for i in range (10):
    forward(num)
    num *= ratio
    right(90)
