from turtle import Turtle


class Updown(Turtle):
    def __init__(self, position):
        super(Updown, self).__init__()
        self.penup()
        self.speed('fastest')
        self.goto(position)
        self.shape('square')
        self.shapesize(10, 43)
        self.color('teal')


class Leftright(Updown):
    def __init__(self, position):
        super(Leftright, self).__init__(position)
        self.shapesize(27, 10)


class Corner(Updown):
    def __init__(self, position):
        super(Corner, self).__init__(position)
        self.shapesize(10, 10)
