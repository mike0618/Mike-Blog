from turtle import Turtle

ALIGN = 'center'
FONT = ('ARIAL', 16, 'bold')


class Borders(Turtle):
    def __init__(self, color='#606060'):
        super(Borders, self).__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color(color)
        self.pensize(3)
        self.penup()
        self.writed = False

    def clear_writed(self):
        self.clear()
        self.writed = False

    def pause(self):
        self.goto(0, -12)
        self.write('PAUSE', False, ALIGN, FONT)
        self.writed = True

    def speedup(self):
        self.goto(330, -225)
        self.write('SPEED UP', False, ALIGN, FONT)
        self.writed = True

    def intersection(self):
        self.goto(-330, 205)
        self.write('INTERSECTION', False, ALIGN, FONT)
        self.writed = True

    def close(self):
        self.goto(380, 225)
        self.write('CLOSE', False, ALIGN, FONT)

    def wrireborders(self):
        # Intersection button
        self.pensize(10)
        self.penup()
        self.goto(-220, 277)
        self.pendown()
        self.goto(-220, 160)
        self.goto(-437, 160)
        # Close button
        self.penup()
        self.goto(320, 277)
        self.pendown()
        self.goto(320, 200)
        self.goto(437, 200)
        # Pause button
        self.penup()
        self.goto(220, -277)
        self.pendown()
        self.goto(220, -160)
        self.goto(437, -160)
        # Speed button
        self.penup()
        self.goto(100, 60)
        self.pendown()
        self.goto(100, -60)
        self.goto(-100, -60)
        self.goto(-100, 60)
        self.goto(100, 60)
        self.goto(100, 60)
        self.goto(320, 200)
        # Arrow buttons
        self.penup()
        self.goto(-220, 160)
        self.pendown()
        self.goto(-100, 60)
        self.penup()
        self.goto(100, -60)
        self.pendown()
        self.goto(220, -160)
        self.penup()
        self.goto(-100, -60)
        self.pendown()
        self.goto(-437, -275)
        # Border
        self.penup()
        self.goto(437, 277)
        self.color('teal')
        self.pendown()
        self.goto(437, -277)
        self.goto(-437, -277)
        self.goto(-437, 277)
        self.goto(437, 277)

    def uparrow(self):
        # Arrows
        self.penup()
        self.goto(0, 138)
        self.pendown()
        self.goto(0, 200)
        self.goto(15, 176)
        self.penup()
        self.goto(-15, 176)
        self.pendown()
        self.goto(0, 200)

    def dnarrow(self):
        self.penup()
        self.goto(0, -138)
        self.pendown()
        self.goto(0, -200)
        self.goto(15, -176)
        self.penup()
        self.goto(-15, -176)
        self.pendown()
        self.goto(0, -200)

    def rarrow(self):
        self.penup()
        self.goto(238, 0)
        self.pendown()
        self.goto(300, 0)
        self.goto(276, 15)
        self.penup()
        self.goto(276, -15)
        self.pendown()
        self.goto(300, 0)

    def larrow(self):
        self.penup()
        self.goto(-238, 0)
        self.pendown()
        self.goto(-300, 0)
        self.goto(-276, 15)
        self.penup()
        self.goto(-276, -15)
        self.pendown()
        self.goto(-300, 0)
