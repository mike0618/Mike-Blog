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
        self.intr_allow = 'NO'
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.on = True
        self.paused = False

    def write_btn(self):
        self.goto(-675, -372)
        self.write("PAUSE", False, ALIGN, FONT)
        self.goto(675, -372)
        self.write("SPEED", False, ALIGN, FONT)
        self.goto(675, 372)
        self.write("CLOSE", False, ALIGN, FONT)

    def writescore(self, num):
        self.clear()
        self.goto(-400, 150)
        self.write(
            f"Intersection allow: {self.intr_allow}\nHigh score: {self.high_score}\nScore: {self.score}\nSpeed: {num}",
            False, 'left', FONT)

    def gameover(self, x=0, y=0):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        # self.score = 0
        self.writescore(0)
        self.home()
        self.write("GAME OVER", False, ALIGN, FONT)
        self.on = False

    def writepause(self):
        self.writescore(0)
        self.home()
        self.write("PAUSED", False, ALIGN, FONT)

    def pause(self, x=0, y=0):
        self.paused = not self.paused

    def intr_switch(self, x=0, y=0):
        if self.intr_allow == 'NO':
            self.intr_allow = 'YES'
        else:
            self.intr_allow = 'NO'
