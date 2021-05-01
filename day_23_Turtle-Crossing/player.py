from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.speed('fastest')
        self.setheading(90)
        self.penup()
        self.go_to_start()
        self.shape('turtle')

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
