import colorgram
import turtle as t
from random import choice

colors = colorgram.extract('image.jpg', 34)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r < 230 or g < 230 or b < 230:
        rgb_colors.append((r, g, b))

tim = t.Turtle()
tim.hideturtle()
tim.penup()
t.colormode(255)
tim.speed(50)


def hirst_paint(dot_size=20, num_dots=10, distance=50):
    a = (num_dots - 1) * distance
    home = -a // 2

    for y in range(0, a + 1, distance):
        for x in range(0, a + 1, distance):
            tim.goto(home + x, home + y)
            tim.dot(dot_size, choice(rgb_colors))


hirst_paint(21, 21, 34)
screen = t.Screen()
screen.exitonclick()
