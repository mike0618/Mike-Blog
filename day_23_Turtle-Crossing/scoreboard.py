from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.home()
        self.write('GAME OVER', False, 'center', FONT)
