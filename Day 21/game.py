from line import MiddleLine
from paddle import Paddle
from ball import Ball
from globals import PADDLE_LOCATIONS_X_AXIS, SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, SCORE_POS, MAX_SPEED
from time import sleep

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.middle_line = MiddleLine(self.screen)
        self.player_one = Paddle(PADDLE_LOCATIONS_X_AXIS[0], SCORE_POS[0])
        self.player_two = Paddle(PADDLE_LOCATIONS_X_AXIS[1], SCORE_POS[1])
        self.ball = Ball()
        self.speed = SPEED
        self.setup_keys()
    
    def setup_keys(self):
        self.screen.onkeypress(self.player_one.up, "w")
        self.screen.onkeypress(self.player_one.down, "s")        
        self.screen.onkeypress(self.player_one.up, "W")
        self.screen.onkeypress(self.player_one.down, "S")
        self.screen.onkeypress(self.player_two.up, "Up")
        self.screen.onkeypress(self.player_two.down, "Down")
    
    def hit_ball(self):
        x_cor = self.ball.xcor()
        return (
            (x_cor < PADDLE_LOCATIONS_X_AXIS[0] + 10 and x_cor > PADDLE_LOCATIONS_X_AXIS[0] and self.ball.distance(self.player_one) <= 50) or 
            (x_cor > PADDLE_LOCATIONS_X_AXIS[1] - 10 and x_cor < PADDLE_LOCATIONS_X_AXIS[1] and self.ball.distance(self.player_two) <= 50)
            )

    def reset_game(self):
        self.ball.reset()
        self.game = True
        self.speed = SPEED

    def play(self):
        self.game = True
        self.playing = True
        while self.playing:
            while self.game:
                # MOVE BALL
                x_pos, y_pos = self.ball.pos()
                half_screen_width = SCREEN_WIDTH // 2
                
                # Detect miss for player one (player two scores)
                if x_pos <= -half_screen_width:
                    self.player_two.increase_score()
                    if self.player_two.get_score() >= 7 and self.player_two.get_score() - self.player_one.get_score() >= 2:
                        # self.player_two.set_winner()
                        self.playing = False
                    self.game = False

                # Detect miss for player two (player one scores)
                if x_pos >= half_screen_width - 10:
                    self.player_one.increase_score()
                    if self.player_one.get_score() >= 7 and self.player_one.get_score() - self.player_two.get_score() >= 2:
                        # self.player_one.set_winner()
                        self.playing = False
                    self.game = False

                # check for paddle bounce
                if self.hit_ball():
                    self.ball.x_bounce()
                    self.speed -= .01

                # check for wall bounce
                if y_pos <= -SCREEN_HEIGHT // 2 + 10 or y_pos >= SCREEN_HEIGHT // 2 - 10:
                    self.ball.y_bounce()

                # move the ball
                self.ball.move()
                self.screen.update()
                speed = max(self.speed, MAX_SPEED)
                sleep(speed)
            
            if self.playing:
                self.reset_game()
        
        input("GAME OVER, SOMEBODY WON")