import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
# timmy.color("green")
t.colormode(255)


def make_square():
    for i in range(0, 4):
        timmy.forward(50)
        timmy.left(90)


def dotted_line():
    for i in range(10):
        timmy.color("black")
        timmy.forward(10)
        timmy.color("white")
        timmy.forward(10)


def shapes(side):
    angle = 360 / side
    for i in range(side):
        timmy.forward(100)
        timmy.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


# for _ in range(3,11):
#     timmy.color(random.choice(color))
#     shapes(_)

walk = (0, 90, 180, 270, 360)


def random_walk():
    timmy.pensize(8)
    timmy.speed("fastest")
    timmy.forward(20)
    angle = random.choice(walk)
    timmy.right(angle)


# for i in range(100):
#     random_color()
#     random_walk()

angle = 0


def spirograph(angle):
    timmy.speed("fastest")
    timmy.pensize(1)
    timmy.circle(150)
    timmy.home()
    timmy.setheading(angle)


for i in range(72):
    angle += 5
    random_color()
    spirograph(angle)

screen = Screen()
screen.exitonclick()
