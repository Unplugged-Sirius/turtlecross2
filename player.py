from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
class Player(Turtle):

        def __init__(self):
            super().__init__()
            self.shape("turtle")
            self.color("green")
            self.penup()
            self.goto(STARTING_POSITION)
            self.lt(90)

        def go_to_start(self):
            if(self.ycor>280):
                self.goto(STARTING_POSITION)
        def up(self):
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)




# from turtle import Turtle
# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280


# class Player(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.shape("turtle")
#         self.setheading(90)
#         self.penup()
#         self.goto(STARTING_POSITION)
#
#
#     def move_up(self):
#         new_y = self.ycor() + MOVE_DISTANCE
#         self.goto(self.xcor(), new_y)
#
#     def go_to_start(self):
#         self.goto(STARTING_POSITION)
#
#     def finishline(self):
#         if self.ycor() > FINISH_LINE_Y:
#             return True
#         else:
#             return False