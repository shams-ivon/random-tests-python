from turtle import Turtle, Screen

arrow_turtle = Turtle()

for _ in range(25):
    arrow_turtle.color("black")
    arrow_turtle.forward(10)
    arrow_turtle.color("white")
    arrow_turtle.forward(10)

# Alternative way

arrow_turtle_2 = Turtle()

arrow_turtle_2.penup()
arrow_turtle_2.goto(0, 100)
arrow_turtle_2.pendown()

for _  in range(25):
    arrow_turtle_2.pendown()
    arrow_turtle_2.forward(10)
    arrow_turtle_2.penup()
    arrow_turtle_2.forward(10)

screen = Screen()
screen.exitonclick()