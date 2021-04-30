from turtle import Screen
from paddles import Paddle, Ball, Wall, X, Y
from board import Score, Velocity
from tkinter import messagebox
from random import randint
from time import sleep


screen = Screen()
screen.title('PyPong Game')
screen.setup(X, Y)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((X // 2 - 50, 0))
l_paddle = Paddle((-(X // 2 - 50), 0))
ball = Ball()
scores = Score()
vel = Velocity()
upwall = Wall((0, Y // 2))
btmwall = Wall((0, -Y // 2))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(ball.velinc, 'Right')
screen.onkey(ball.veldec, 'Left')
screen.onkey(ball.end_game, 'Escape')
screen.onkey(ball.pause_game, 'p')
screen.onkeypress(upwall.psyon, 'space')
screen.onkeyrelease(upwall.psyoff, 'space')

messagebox.showinfo('Welcome to PyPong!',
                    'UP/DOWN: move right paddle\n'
                    'W/S    : move left paddle\n'
                    'RIGHT/LEFT : velocity\n'
                    '\nSPACE : !warning! psychedelic mode\n'
                    'can cause an epileptic seizure\n'
                    '\nP     : pause\n'
                    'ESC    : exit')


def pong():
    while not ball.paused and ball.on:
        if upwall.psy:
            screen.bgcolor('#' + str("%06x" % randint(0, 0xFFFFFF)))
        ball.move()
        bx = ball.xcor()
        by = ball.ycor()
        ry = r_paddle.ycor()
        ly = l_paddle.ycor()
        if abs(bx) == X // 2 - 70:
            if (abs(ry - by) <= 50 and bx > 0) or (abs(ly - by) <= 50 and bx < 0):
                ball.velinc()
                ball.bounce_x()
                ball.randcolor()
                if bx > 0:
                    r_paddle.randcolor()
                else:
                    l_paddle.randcolor()
        elif abs(ball.xcor()) > X // 2:
            ball.veldec()
            if ball.xcor() > 0:
                scores.lpoint()
            else:
                scores.rpoint()
            ball.home()
            ball.bounce_x()
            scores.update()
        vel.vupdate(ball.vel)
        screen.update()

while ball.on:
    sleep(0.2)
    pong()
    screen.update()
