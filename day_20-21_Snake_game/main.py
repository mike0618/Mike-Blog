from turtle import Screen
from snake import Snake
from food import Food, Bonus
from board import Writebrd, Border
from tkinter import messagebox


def snake_game():
    screen = Screen()
    screen.setup(880, 560, 520)
    screen.bgcolor('#363636')
    screen.title('My PySnake Game')
    screen.tracer(0)
    Border()

    messagebox.showinfo("Welcome to PySnake!",
                     "Controls:\n"
                     "Turn the snake:       Arrow keys\n"
                     "Speed-up:                Space\n"
                     "Intersection allow:   I")

    snake = Snake(3)
    intrboard = Writebrd()
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkeypress(snake.speed_up, 'space')
    screen.onkeyrelease(snake.speed_down, 'space')
    screen.onkey(intrboard.intr_switch, 'i')
    screen.onkeyrelease(screen.bye, 'Escape')

    # food = Food()
    food = [
        Food(),
        Bonus((420, 260)),
        Bonus((-420, -260)),
        Bonus((-420, 260)),
        Bonus((420, -260)), ]
    scoreboard = Writebrd()
    speedboard = Writebrd()

    game_on = True
    while game_on:

        snake.move()
        speedboard.writespeed(snake.speed)
        intrboard.check_intr()
        # Detect collision with food.
        for piece in food:
            if snake.head.distance(piece) < 10:
                food[0].refresh()
                snake.extend()
                scoreboard.score += 1
                scoreboard.writescore()
                if not scoreboard.score % 5:
                    snake.speed += 1
        # Detect collision with wall.
        snake_x = snake.head.xcor()
        snake_y = snake.head.ycor()
        if abs(snake_x) > 420 or abs(snake_y) > 260:
            scoreboard.gameover()
            game_on = False
        # Detect collision with tail.
        if intrboard.intr_allow == 'NO':
            for sgm in snake.snake[1:]:
                if snake.head.distance(sgm) < 10:
                    scoreboard.gameover()
                    game_on = False
                    break
        screen.update()
    screen.clear()


retry = True
while retry:
    snake_game()
    retry = messagebox.askyesno(None, 'Try anain?')
