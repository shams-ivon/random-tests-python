from turtle import Turtle, Screen

arrow_turtle = Turtle()
arrow_turtle.width(4)

for _ in range(4):
    arrow_turtle.forward(100)
    arrow_turtle.right(90)

screen = Screen()
screen.exitonclick()