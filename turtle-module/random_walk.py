import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

arrow_turtle = Turtle()
arrow_turtle.width(10)

def random_color():
    r = random.randint(10, 255)
    g = random.randint(10, 255)
    b = random.randint(10, 255)
    return tuple((r, g, b))

for _ in range(200):
    option = random.randrange(3)
    angles = [0, 90, 180, 270]
    arrow_turtle.color(random_color())
    arrow_turtle.left(angles[random.randrange(3)])
    arrow_turtle.speed(0)

    arrow_turtle.forward(20)

screen.exitonclick()