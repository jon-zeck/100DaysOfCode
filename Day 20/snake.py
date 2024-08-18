from turtle import Turtle
import time
from score import Score

SHAPESIZE = 1
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

# SNAKE SETTINGS
SNAKE_LENGTH = 5
SNAKE_SPEED = .1

class Snake():
    def __init__(self, colour, location) -> None:
        self.segments = []
        self.head = None
        self.speed = SNAKE_SPEED
        self.colour = colour
        self.location = location
        self.size = 0
        self.created = False
        self.create_snake()
    
    def create_snake(self):
        self.created = True
        for _ in range(SNAKE_LENGTH):
            self.append_segment()
        if self.segments:
            self.head = self.segments[0]

    def append_segment(self):
        if not self.created:
            return
        segment = Turtle("square")
        segment.color(self.colour)
        segment.penup()
        segment.shapesize(SHAPESIZE, SHAPESIZE)
        segment.setpos(self.location["x"] + self.size, self.location["y"])
        self.size -= MOVE_DISTANCE * SHAPESIZE
        self.segments.append(segment)
    
    def reset(self):
        if not self.created:
            return
        for segment in self.segments:
            segment.reset()
            segment.hideturtle()
        for _ in range(len(self.segments)):
            self.segments.pop()
        self.size = 0
        self.create_snake()

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prior_seg = self.segments[seg_num - 1]
            newx = prior_seg.xcor()
            newy = prior_seg.ycor()
            self.segments[seg_num].setpos(newx, newy)
        
        self.head.forward(MOVE_DISTANCE * SHAPESIZE) # move the head forward 20
        time.sleep(self.speed)

    def up(self):
        if not self.created:
            return
        heading = self.head.heading()
        if heading == UP or heading == DOWN:
            return
        self.head.setheading(UP)
    
    def left(self):
        if not self.created:
            return
        heading = self.head.heading()
        if heading == LEFT or heading == RIGHT:
            return
        self.head.setheading(LEFT)
    
    def right(self):
        if not self.created:
            return
        heading = self.head.heading()
        if heading == RIGHT or heading == LEFT:
            return
        self.head.setheading(RIGHT)

    def down(self):
        if not self.created:
            return
        heading = self.head.heading()
        if heading == DOWN or heading == UP:
            return
        self.head.setheading(DOWN)