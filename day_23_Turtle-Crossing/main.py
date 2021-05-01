import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle Crossing')
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
    py = player.ycor()
    # Detect collision with car
    for car in car_manager.cars:
        cy = car.ycor()
        if cy > 0:
            car.back(car_manager.car_speed)
        else:
            car.forward(car_manager.car_speed)
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
