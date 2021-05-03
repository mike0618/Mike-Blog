from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 16, 'normal')
X = 440
Y = 280


class Writebrd(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.intr_allow = False
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.on = True
        self.paused = False

    def writescore(self, num):
        self.clear()
        self.goto(-400, -250)
        self.write(
            f"High score: {self.high_score}\nScore: {self.score}\nSpeed: {num}",
            False, 'left', FONT)

    def gameover(self, x=0, y=0):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        self.on = False

    def pause(self, x=0, y=0):
        self.paused = not self.paused

    def intr_switch(self, x=0, y=0):
        if not self.intr_allow:
            self.intr_allow = True
        else:
            self.intr_allow = False

    def control(self, x, y):
        if -420 < x < -220 and 260 > y > 140:
            self.intr_switch()
        elif abs(x) < 100 and abs(y) < 60:
            self.paused = not self.paused
        elif 420 > x > 320 and 260 > y > 200:
            self.gameover()
        else:
            return True
