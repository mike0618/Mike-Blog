from turtle import Turtle, Screen, colormode
from random import choice, randint

timmy = Turtle()
timmy.shape('turtle')
colormode(255)
offset = randint(0, 360)


def random_color():
    # return '#' + str("%06x" % randint(0, 0xFFFFFF))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def geometry_fig(num, star=False):
    if star and num % 2:
        angle = 180 - 180 / num
    else:
        angle = 360 / num
    timmy.begin_fill()
    for i in range(num):
        timmy.forward(100)
        timmy.left(angle)
    timmy.end_fill()


def random_walk(num, triangle=False):
    timmy.speed(5)
    timmy.pensize(8)
    directions = [0, 90, 180, 270]
    if triangle:
        directions = [0, 120, 240]

    for _ in range(num):
        timmy.color(random_color())
        timmy.setheading(choice(directions) + offset)
        timmy.forward(21)


def spirograph(tilt, extent):
    timmy.speed(100)
    steps = extent // 3
    timmy.setheading(offset)
    for _ in range(360 // tilt):
        timmy.color(random_color())
        timmy.begin_fill()
        timmy.circle(100, extent, steps)
        timmy.end_fill()
        timmy.left(tilt)


spirograph(10, 365)
random_walk(100)
random_walk(150, True)

for n in range(10, 2, -1):
    timmy.color(random_color(), random_color())
    geometry_fig(n)

for n in range(5, 8, 2):
    timmy.color(random_color(), random_color())
    timmy.forward(100)
    geometry_fig(n, True)

for _ in range(13):
    timmy.color(random_color())
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()
