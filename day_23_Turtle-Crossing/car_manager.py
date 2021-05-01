from turtle import Turtle
from random import choice, randint

STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        self.y = choice(range(-240, 241, 30))
        if randint(1, 30 // self.car_speed) == 1 and abs(self.y) > 0:
            car = Turtle('square')
            car.penup()
            car.shapesize(1, 2)
            car.color('#' + str("%06x" % randint(0x363636, 0xFFFFFF)))
            if self.y > 0:
                car.goto(320, self.y)
            else:
                car.goto(-320, self.y)
            self.cars.insert(0, car)


    def move(self):
        for car in self.cars[:50]:
            if car.ycor() > 0:
                car.back(self.car_speed)
            else:
                car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += STARTING_MOVE_DISTANCE
