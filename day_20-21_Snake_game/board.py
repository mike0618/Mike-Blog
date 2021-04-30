from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 16, 'normal')
X = 440
Y = 280


class Writebrd(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.intr_allow = 'NO'
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.on = True
        self.paused = False

    def writescore(self):
        self.goto(-250, 240)
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def writespeed(self, num):
        self.goto(-360, 240)
        self.clear()
        self.write(f"Speed: {num}", False, ALIGN, FONT)

    def gameover(self):
        self.home()
        self.write("GAME OVER", False, ALIGN, FONT)
        self.on = False

    def writepause(self):
        self.home()
        self.write("PAUSED", False, ALIGN, FONT)
        self.clear()

    def pause(self):
        self.paused = not self.paused

    def check_intr(self):
        self.goto(300, 240)
        self.clear()
        self.write(f"Intersection allow: {self.intr_allow}", False, ALIGN, FONT)

    def intr_switch(self):
        if self.intr_allow == 'NO':
            self.intr_allow = 'YES'
        else:
            self.intr_allow = 'NO'


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.color('teal')
        self.pensize(20)
        self.penup()
        self.goto(-X, -Y)
        self.pendown()
        self.goto(-X, Y)
        self.goto(X, Y)
        self.goto(X, -Y)
        self.goto(-X, -Y)
