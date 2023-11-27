from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(100)


def move_backward():
    timmy.backward(100)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)
    # new_turtle.left(45)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)
    # new_turtle.right(45)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
move = input()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()