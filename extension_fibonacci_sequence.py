# fibonacci_sequence.py

from turtle import *

# print("0")
# print("1")

for i in range (10):
    penup()
    goto(0,0)
    pendown()
    a = 0
    b = 1

    while a < 100:
        c = a+b
        # print(c)
        a = b
        b = c
        forward(c)
        left(60)
    left(36)

input()