import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create()
    car_manager.move()

    #detect collision
    for car in car_manager.allcars:
        print (car.distance(player))
        if player.distance(car) < 25:
            game_is_on == False


# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import ScoreBoard
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
#
# player = Player()
# car_manager = CarManager()
# scoreboard = ScoreBoard()
#
# screen.listen()
# screen.onkey(player.move_up, "Up")
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     car_manager.create_car()
#     car_manager.move_cars()
#
#     # Detect player collision with car
#     for car in car_manager.all_cars:
#         print (player.distance(car))
#         if player.distance(car) < 25:
#             scoreboard.game_over()
#             game_is_on = False
#             screen.exitonclick()
#
#     # safely reached to a finish line
#     if player.finishline():
#         player.go_to_start()
#         car_manager.speed_up()
#         scoreboard.score_up()