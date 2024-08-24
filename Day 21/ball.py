from line import Line
import random
from globals import SCREEN_WIDTH, BALL_SPEED, SCREEN_HEIGHT

class Ball(Line):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5)
        self.showturtle()
        self.x_move = 10
        self.y_move = 10        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def x_bounce(self):
        self.x_move = -self.x_move

    def y_bounce(self):
        self.y_move = -self.y_move
    
    def reset(self):
        self.setpos(0, 0)
