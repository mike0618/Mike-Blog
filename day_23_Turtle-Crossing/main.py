import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
board = Scoreboard()
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    car_manager.create()
    car_manager.move()
    py = player.ycor()
    # Detect collision with car
    for car in car_manager.cars[-50:]:
        cy = car.ycor()
        if player.distance(car) < 30 and py - cy < 20 and cy - py < 25:
            game_is_on = False
            board.game_over()
    # Detect successful crossing
    if player.at_finish():
        player.go_to_start()
        car_manager.level_up()
        board.level_up()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
