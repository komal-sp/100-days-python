import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)
# slowest speed
timmy.speed(5)
colours = ['indigo', 'medium violet red', 'dark orange', 'olive drab', 'navy', 'dodger blue', 'dark cyan']
directions = [0, 90, 180, 270]


def dash_line():
    for i in range(50):
        if i % 2 != 0:
            timmy.penup()
        else:
            timmy.pendown()
        timmy.forward(10)


def diff_shapes():
    for i in range(3, 8):
        angle = 360 // i
        timmy.color(random.choice(colours))
        for j in range(i):
            timmy.forward(100)
            timmy.right(angle)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    while True:
        timmy.color(random.choice(colours))
        # new_turtle.color(random_colour())
        angle = random.choice(directions)
        timmy.forward(30)
        timmy.left(angle)


def random_circle(size_of_gap):
    """Spirograph"""
    timmy.speed(50)
    angle = int(360/size_of_gap)
    for i in range(angle):
        timmy.color(random_colour())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + 10)


# dash_line()
# diff_shapes()
# random_walk()
random_circle(10)
t.exitonclick()