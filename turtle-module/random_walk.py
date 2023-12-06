import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

arrow_turtle = Turtle()
arrow_turtle.width(5)

def random_color():
    rgb = [10, 30, 80, 120, 170, 240]
    random.shuffle(rgb)
    return tuple(rgb[0:3])

for _ in range(200):
    option = random.randrange(3)
    arrow_turtle.color(random_color())
    arrow_turtle.speed(0)

    if option == 1:
        arrow_turtle.left(90)
    elif option == 2: 
        arrow_turtle.right(90)
    elif option == 3:
        arrow_turtle.left(180)

    arrow_turtle.forward(20)

screen.exitonclick()