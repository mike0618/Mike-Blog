from turtle import Screen
from snake import Snake
from food import Food, Bonus
from board import Writebrd
from tkinter import messagebox
from time import sleep
from borders import Borders


def snake_game():
    screen = Screen()
    screen.clear()
    screen.setup(880, 560)
    screen.bgcolor('#363636')
    screen.title('My PySnake Game')
    screen.tracer(0)

    messagebox.showinfo("Welcome to PySnake!",
                        "Controls:\n"
                        "Turn the snake:       Arrow keys\n"
                        "Speed-up:                Space\n"
                        "Intersection allow:   I\n"
                        "Pause:                    P\n"
                        "End game:             ESC")

    snake = Snake(3)
    scoreboard = Writebrd()
    Borders()
    with open('data.txt') as f:
        cont = f.read()
        if cont.isdigit():
            scoreboard.high_score = int(cont)

    def control(x, y):
        if scoreboard.control(x, y):
            snake.control(x, y)

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkeypress(snake.speed_up, 'space')
    screen.onkeyrelease(snake.speed_down, 'space')
    screen.onkey(scoreboard.intr_switch, 'i')
    screen.onkey(scoreboard.gameover, 'Escape')
    screen.onkey(scoreboard.pause, 'p')
    screen.onclick(control)

    food = [
        Food(),
        Bonus((420, 260)),
        Bonus((-420, -260)),
        Bonus((-420, 260)),
        Bonus((420, -260)), ]

    def play():
        while scoreboard.on and not scoreboard.paused:
            snake.move()
            scoreboard.writescore(snake.speed)
            # Detect collision with food.
            for piece in food:
                if snake.head.distance(piece) < 10:
                    food[0].refresh()
                    snake.extend()
                    scoreboard.score += 1
                    if not scoreboard.score % 5:
                        snake.speed += 1
            # Detect collision with wall.
            snake_x = snake.head.xcor()
            snake_y = snake.head.ycor()
            screen.update()
            if abs(snake_x) > 420 or abs(snake_y) > 260:
                scoreboard.gameover()
            # Detect collision with tail.
            if scoreboard.intr_allow == 'NO':
                for sgm in snake.snake[1:]:
                    if snake.head.distance(sgm) < 10:
                        scoreboard.gameover()
                        break
            if scoreboard.paused:
                scoreboard.writepause()
            if not scoreboard.on:
                scoreboard.gameover()

    while scoreboard.on:
        play()
        screen.update()
        sleep(0.2)


retry = True
while retry:
    snake_game()
    retry = messagebox.askyesno('PySnake', 'Play again?')
