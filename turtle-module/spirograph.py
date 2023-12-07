from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

arrow_turtle = Turtle()
arrow_turtle.width(2)

def random_color():
    r = random.randint(10, 255)
    g = random.randint(10, 255)
    b = random.randint(10, 255)
    return tuple((r, g, b))

for _ in range(36):
    arrow_turtle.color(random_color())
    arrow_turtle.speed(0)
    arrow_turtle.circle(100)
    arrow_turtle.left(10)

screen.exitonclick()