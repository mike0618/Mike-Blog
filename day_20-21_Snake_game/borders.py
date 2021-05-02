from turtle import Turtle

ALIGN = 'center'
FONT = ('ARIAL', 16, 'bold')


class Borders(Turtle):
    def __init__(self):
        super(Borders, self).__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color('#606060')
        self.pensize(10)
        self.penup()
        # Write
        self.goto(0, -12)
        self.write('SPEED UP', False, ALIGN, FONT)
        self.goto(-330, 205)
        self.write('INTERSECTION', False, ALIGN, FONT)
        self.goto(380, 225)
        self.write('CLOSE', False, ALIGN, FONT)
        self.goto(330, -225)
        self.write('PAUSE', False, ALIGN, FONT)
        # Intersection button
        self.goto(-220, 280)
        self.pendown()
        self.goto(-220, 160)
        self.goto(-440, 160)
        # Close button
        self.penup()
        self.goto(320, 280)
        self.pendown()
        self.goto(320, 200)
        self.goto(440, 200)
        # Pause button
        self.penup()
        self.goto(220, -280)
        self.pendown()
        self.goto(220, -160)
        self.goto(440, -160)
        # Speed button
        self.penup()
        self.goto(80, 50)
        self.pendown()
        self.goto(80, -50)
        self.goto(-80, -50)
        self.goto(-80, 50)
        self.goto(80, 50)
        self.goto(80, 50)
        self.goto(320, 200)
        # Arrow buttons
        self.penup()
        self.goto(-220, 160)
        self.pendown()
        self.goto(-80, 50)
        self.penup()
        self.goto(80, -50)
        self.pendown()
        self.goto(220, -160)
        self.penup()
        self.goto(-80, -50)
        self.pendown()
        self.goto(-440, -275)
        # Arrows
        self.penup()
        self.goto(0, 130)
        self.pendown()
        self.goto(0, 200)
        self.goto(10, 173)
        self.goto(-10, 173)
        self.goto(0, 200)

        self.penup()
        self.goto(0, -130)
        self.pendown()
        self.goto(0, -200)
        self.goto(10, -173)
        self.goto(-10, -173)
        self.goto(0, -200)

        self.penup()
        self.goto(200, 0)
        self.pendown()
        self.goto(300, 0)
        self.goto(260, 10)
        self.goto(260, -10)
        self.goto(300, 0)

        self.penup()
        self.goto(-200, 0)
        self.pendown()
        self.goto(-300, 0)
        self.goto(-260, 10)
        self.goto(-260, -10)
        self.goto(-300, 0)

        # Border
        self.penup()
        self.goto(440, 280)
        self.color('teal')
        self.pensize(16)
        self.pendown()
        self.goto(440, -280)
        self.goto(-440, -280)
        self.goto(-440, 280)
        self.goto(440, 280)


