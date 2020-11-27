import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()

screen.onkey(player.move, 'Up')

game_is_on = True
current_level=1
speed=0.1

while game_is_on:
    time.sleep(speed)
    screen.update()
    car.move_car()

    #check collision
    for dummy_car in car.cars:
        if dummy_car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on=False

    # level up
    # speed up
    if player.ycor() > 250:
        scoreboard.level_up()
        player.player_reset()
        speed*=.5

        pass

screen.exitonclick()

