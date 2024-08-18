from turtle import Turtle
import random

'''
Food Class:
    - Attributes:
        - pos.x
        - pos.y
    - Methods:
        - new_location()
'''

FOOD_SHAPE_MULTIPLIER = 0.5
MARGIN = 10
SQUARE_SIZE = 20
FOOD_COLOUR = "#ffff00"

class Food(Turtle):
    def __init__(self, screen_size) -> None:
        super().__init__()
        self.shape("square")
        self.color(FOOD_COLOUR)
        self.penup()
        self.shapesize(FOOD_SHAPE_MULTIPLIER, FOOD_SHAPE_MULTIPLIER)
        self.speed("fastest")
        self.screen_size = int(screen_size / 2)
        self.spawn_food()

    def spawn_food(self):
        rand_x = random.randint(-(self.screen_size - MARGIN), self.screen_size - MARGIN)
        rand_y = random.randint(- (self.screen_size - MARGIN), self.screen_size - MARGIN)
        rounded_x = self.round_base_20(rand_x)
        rounded_y = self.round_base_20(rand_y)
        self.goto(rounded_x, rounded_y)

    def round_base_20(self, x):
        return SQUARE_SIZE * round(x / SQUARE_SIZE)
    
    def reset(self):
        super().reset()
        self.hideturtle()
    
    