from turtle import Screen, Turtle
import random

screen = Screen()
screen.colormode(255)

arrow_turtle = Turtle()
arrow_turtle.width(4)

total_angle = 0

def random_color():
    rgb = [10, 30, 80, 120, 170, 240]
    random.shuffle(rgb)
    return tuple(rgb[0:3])


for polygon_size in range(3, 11):
    total_angle += 180
    each_angle = total_angle / polygon_size
    turn_angle = 180 - each_angle
    arrow_turtle.color(random_color())

    for side in range(polygon_size):
        arrow_turtle.forward(100)
        arrow_turtle.right(turn_angle)

screen.exitonclick()