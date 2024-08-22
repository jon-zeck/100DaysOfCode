from turtle import Turtle
from globals import LINE_SHAPE, LINE_RESIZEMODE, LINE_COLOUR, SCREEN_HEIGHT, MIDDLE_LINE_HEIGHT, MIDDLE_LINE_WIDTH
import math
from time import sleep

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape(LINE_SHAPE)
        self.resizemode(LINE_RESIZEMODE)
        self.color(LINE_COLOUR)
        self.speed("fastest")
        self.penup()

class SmallRect(Line):
    def __init__(self, y_axis):
        super().__init__()
        self.shapesize(0.5, MIDDLE_LINE_WIDTH, 0)
        self.setpos(0, y_axis)
        self.showturtle()

class MiddleLine():
    def __init__(self, screen):
        self.line = []
        self.screen = screen
        self.draw_middle_line()

    def draw_middle_line(self):
        half_screen = SCREEN_HEIGHT // 2
        for i in range(-half_screen, half_screen, MIDDLE_LINE_HEIGHT * 2):
            self.line.append(SmallRect(i))
            # sleep(0.1)
            self.screen.update()
