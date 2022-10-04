from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-260, 260)
            new_car.goto(300, new_y)
            self.car.append(new_car)

    def move(self):
        for cars in self.car:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
