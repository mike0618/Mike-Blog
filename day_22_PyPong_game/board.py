from turtle import Turtle
from paddles import X, Y, VEL

ALIGN = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.color('teal')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.x = X // 2 - 100
        self.y = Y // 2 - 50
        self.update()

    def update(self):
        self.clear()
        self.goto(-self.x, self.y)
        self.write(self.l_score, False, ALIGN, FONT)
        self.goto(self.x, self.y)
        self.write(self.r_score, False, ALIGN, FONT)

    def lpoint(self):
        self.l_score += 1

    def rpoint(self):
        self.r_score += 1

class Velocity(Score):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vupdate(VEL)

    def vupdate(self, vel):
        self.clear()
        self.goto(0, self.y)
        self.write(f'Velocity: {vel}', False, ALIGN, FONT)
