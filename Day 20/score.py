from turtle import Turtle
import math
from globals import SET_MOVE_FALSE, ALIGNMENT, GAME_OVER_FONT, SCORE_FONT

class Text(Turtle):
    def __init__(self, text="", location={"x":0, "y":0}):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(location["x"], location["y"])
        self.text = text
    
    def write_text(self):
        self.write(self.text, SET_MOVE_FALSE, ALIGNMENT, GAME_OVER_FONT)

class Score(Text):
    def __init__(self, location):
        super().__init__("", location)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", SET_MOVE_FALSE, ALIGNMENT, SCORE_FONT)

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.increase_score()
        self.write_score()

    def write_time(self):
        self.clear()
        score_string = "%.1f" % self.score
        if self.score < 0:
            score_string = "0.0"
        self.write(f"Time: {score_string}", SET_MOVE_FALSE, ALIGNMENT, SCORE_FONT)

    def update_timer(self, seconds):
        self.score = seconds
        self.write_time()
        
    def reset(self):
        self.score = 0
        self.write_score()

    def half_score(self):
        self.score = math.floor(self.score / 2)
        self.write_score()
    