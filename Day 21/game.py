from line import MiddleLine
from paddle import Paddle
from globals import PADDLE_LOCATIONS_X_AXIS

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.middle_line = MiddleLine(self.screen)
        self.player_one = Paddle(PADDLE_LOCATIONS_X_AXIS[0])
        self.player_two = Paddle(PADDLE_LOCATIONS_X_AXIS[1])
        self.setup_keys()
    
    def setup_keys(self):
        self.screen.onkey(self.player_one.up, "w")
        self.screen.onkey(self.player_one.down, "s")        
        self.screen.onkey(self.player_one.up, "W")
        self.screen.onkey(self.player_one.down, "S")
        self.screen.onkey(self.player_two.up, "Up")
        self.screen.onkey(self.player_two.down, "Down")