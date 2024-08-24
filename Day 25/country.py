from turtle import Turtle
class Country(Turtle):
    def __init__(self, data):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(data.x.values[0], data.y.values[0])
        self.write(data.state.values[0])
    