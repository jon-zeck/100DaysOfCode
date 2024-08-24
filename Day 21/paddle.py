from line import Line
from globals import PADDLE_HEIGHT, PADDLE_HEIGHT_PX, PADDLE_WIDTH, MOVE_CHUNK, SCREEN_HEIGHT
from score import Score

class Paddle(Line):
    def __init__(self, x_axis, score_loc):
        super().__init__()
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH, 0)
        self.setpos(x_axis, 0)
        self.score = Score(score_loc)
        self.showturtle()
    
    def get_score(self):
        return self.score.score

    def increase_score(self):
        self.score.increase_score()
        self.score.update_scoreboard()

    def up(self):
        playeable_height = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT_PX // 2)
        x_pos, y_pos = self.pos()
        # print(f"y: {y_pos}, ph: {playeable_height}")
        if y_pos >= playeable_height:
            return
        self.setpos(x_pos, y_pos + MOVE_CHUNK)

    def down(self):
        playeable_height = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT_PX // 2) - MOVE_CHUNK
        x_pos, y_pos = self.pos()
        # print(f"y: {y_pos}, ph: {playeable_height}")
        if y_pos <= -playeable_height:
            return
        self.setpos(x_pos, y_pos - MOVE_CHUNK)
