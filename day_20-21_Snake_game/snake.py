from turtle import Turtle
from time import sleep

MOVE_DIST = 20
START_X = 0
START_Y = 0

class Snake:
    def __init__(self, length):
        self.length = length
        self.speed = 3
        self.snake = []
        self.x = START_X
        self.paused = False
        for i in range(self.length):
            self.x -= MOVE_DIST
            self.add_turtle((self.x, START_Y))
        self.head = self.snake[0]

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
            self.head.setheading(angle)

    def left(self):
        self.direction(180)

    def right(self):
        self.direction(0)

    def up(self):
        self.direction(90)

    def down(self):
        self.direction(270)

    def speed_up(self):
        self.speed *= 2

    def speed_down(self):
        self.speed //= 2

    def pause(self):
        self.paused = not self.paused
