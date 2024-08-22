from line import Line
from globals import PADDLE_HEIGHT, PADDLE_WIDTH, MOVE_CHUNK

class Paddle(Line):
    def __init__(self, x_axis):
        super().__init__()
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH, 0)
        self.setpos(x_axis, 0)
        self.showturtle()
    
    def up(self):
        x_pos, y_pos = self.pos()
        self.setpos(x_pos, y_pos + MOVE_CHUNK)

    def down(self):
        x_pos, y_pos = self.pos()
        self.setpos(x_pos, y_pos - MOVE_CHUNK)
