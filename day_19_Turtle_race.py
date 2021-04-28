from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=800, height=500, startx=560)
colors = ['red', 'gold', 'green', 'cyan', 'blue', 'magenta']
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color: \n"
                                                          f"{' / '.join(colors)}")
turtles = []
y = -200
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-370, y)
    turtles.append(new_turtle)
    y += 80

while True:
    turtle_go = choice(turtles)
    turtle_go.setheading(randint(330, 390))
    turtle_go.forward(randint(1, 10))
    if turtle_go.xcor() > 399:
        win_color = turtle_go.pencolor()
        if win_color == user_bet:
            print(f"You win! The {win_color} turtle is the winner!")
        else:
            print(f"You lose. The {win_color} turtle is the winner!")
        break


screen.exitonclick()
