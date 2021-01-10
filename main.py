import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

the_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(the_turtle.move_up, "w")


game_is_on = True
initial_speed = 0.1
while game_is_on:
    time.sleep(initial_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(the_turtle) < 20:
            game_is_on = False
            scoreboard.deploy_game_over()

    # Detect successful crossing
    if the_turtle.is_at_finish_line():
        initial_speed *= 0.7
        the_turtle.reset_turtle()
        scoreboard.level_up()

screen.exitonclick()
