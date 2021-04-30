from turtle import Turtle
from time import sleep
from random import randint

X = 1000
Y = 600
VEL = 8
MOVE_DIST = 20

class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.speed('fastest')
        self.goto(position)
        self.shape('square')
        self.shapesize(5, 3)
        self.randcolor()
        self.y_lim = (Y - self.shapesize()[0] * MOVE_DIST) // 2 - MOVE_DIST
        self.ondrag(self.dragging)

    def dragging(self, x, y):
        self.goto(self.xcor(), y)
        self.ondrag(self.dragging)

    def up(self):
        if self.ycor() < self.y_lim:
            self.goto(self.xcor(), self.ycor() + MOVE_DIST * 2)

    def down(self):
        if self.ycor() > -self.y_lim:
            self.goto(self.xcor(), self.ycor() - MOVE_DIST * 2)

    def randcolor(self):
        self.color('#' + str("%06x" % randint(0x363636, 0xFFFFFF)))


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.vel = VEL
        self.speed('fastest')
        self.shape('circle')
        self.randcolor()
        self.xinc = 5
        self.yinc = 5
        self.paused = False
        self.on = True

    def move(self):
        if abs(self.ycor()) == Y // 2 - 20:
            self.bounce_y()
        self.goto(self.xcor() + self.xinc, self.ycor() + self.yinc)
        sleep(0.25 / self.vel)

    def bounce_x(self):
        self.xinc *= -1

    def bounce_y(self):
        self.yinc *= -1

    def velinc(self):
        self.vel += 1

    def veldec(self):
        if self.vel > 1:
            self.vel -= 1

    def randcolor(self):
        self.color('#' + str("%06x" % randint(0x363636, 0xFFFFFF)))

    def pause_game(self):
        self.paused = not self.paused

    def end_game(self):
        self.on = False


class Wall(Turtle):
    def __init__(self, position):
        super(Wall, self).__init__()
        self.penup()
        self.speed('fastest')
        self.goto(position)
        self.shape('square')
        self.shapesize(1, X // 20)
        self.color('teal')
        self.psy = False

    def psyon(self):
        self.psy = True

    def psyoff(self):
        self.psy = False
