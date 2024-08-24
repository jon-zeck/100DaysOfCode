from turtle import Turtle
from globals import SET_MOVE_FALSE, ALIGNMENT, SCORE_FONT

class Score(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("grey")
        self.goto(location["x"], location["y"])
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}", SET_MOVE_FALSE, ALIGNMENT, SCORE_FONT)

    def increase_score(self):
        self.score += 1

    def reset(self):
        self.score = 0
        self.update_scoreboard()
    