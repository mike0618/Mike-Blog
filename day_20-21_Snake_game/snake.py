from turtle import Turtle
from time import sleep
from math import ceil
from borders import Borders

MOVE_DIST = 20
START_X = 0
START_Y = 0


class Snake:
    def __init__(self, length):
        self.length = length
        self.speed = 3
        self.speedup =  False
        self.snake = []
        self.x = START_X
        for i in range(self.length):
            self.x -= MOVE_DIST
            self.add_turtle((self.x, START_Y))
        self.head = self.snake[0]
        self.arrows = Borders('#9D9D9D')

    def add_turtle(self, position):
        new_turtle = Turtle(shape='square')
        if len(self.snake) % 2:
            new_turtle.color('lightgreen')
        else:
            new_turtle.color('gold')
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)

    def extend(self):
        self.add_turtle(self.snake[-1].position())

    def move(self):
        sleep(1 / self.speed)
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[seg_num - 1].pos()
            self.snake[seg_num].goto(new_pos)
        self.snake[0].forward(MOVE_DIST)

    def direction(self, angle):
        if abs(self.head.heading() - angle) != 180:
            if angle == 0:
                self.arrows.clear()
                self.arrows.rarrow()
            elif angle == 90:
                self.arrows.clear()
                self.arrows.uparrow()
            elif angle == 180:
                self.arrows.clear()
                self.arrows.larrow()
            elif angle == 270:
                self.arrows.clear()
                self.arrows.dnarrow()
            self.head.setheading(angle)

    def left(self, x=0, y=0):
        self.direction(180)

    def right(self, x=0, y=0):
        self.direction(0)

    def up(self, x=0, y=0):
        self.direction(90)

    def down(self, x=0, y=0):
        self.direction(270)

    def speed_up(self, x=0, y=0):
        self.speed *= 2
        self.speedup = True

    def speed_down(self, x=0, y=0):
        self.speed = ceil(self.speed / 2)
        self.speedup = False

    def control(self, x, y):
        if 420 > x > 220 and -260 < y < -140:
            if self.speedup:
                self.speed = ceil(self.speed / 2)
                self.speedup = False
            else:
                self.speed *= 2
                self.speedup = True
        elif 420 > x > 0 and abs(y) < x / 1.618:
            self.right()
        elif -420 < x < 0 and abs(y) < -x / 1.618:
            self.left()
        elif 260 > y > 0 and abs(x) < y * 1.618:
            self.up()
        elif -260 < y < 0 and abs(x) < -y * 1.618:
            self.down()



