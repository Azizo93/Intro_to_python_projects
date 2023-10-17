from turtle import *
from random import randint

omar = Turtle()
omar.color('blue')
omar.shape('turtle')
omar.penup()
omar.goto(-160, 100)
omar.pendown()

john = Turtle()
john.color('green')
john.shape('turtle')
john.penup()
john.goto(-160, 70)
john.pendown()

bob = Turtle()
bob.color('red')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 40)
bob.pendown()

for movement in range(100):
    omar.forward(randint(1,5))
    john.forward(randint(1,5))
    bob.forward(randint(1,5))

x = input("Press enter to close")

