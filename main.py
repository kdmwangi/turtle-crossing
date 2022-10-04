import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()
    # if player.distance(car_manager.car) < 20:
    #     print("hit by a car")
    for cars in car_manager.car:
        if cars.distance(player) < 20:
            print("hit by car")
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        print("Switch to another level")
        car_manager.level_up()

        scoreboard.increase_level()
        player.goto(0, -280)

screen.exitonclick()
