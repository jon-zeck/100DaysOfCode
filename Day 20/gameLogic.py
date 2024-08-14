from food import Food
from snake import Snake
from score import Score
import time

# SNAKE SETTINGS
SNAKE_COLOURS = ["white", "black"]
SNAKE_LOCATIONS = [{"x": -280, "y": 200}, {"x": -280, "y": -200}]

# SCORE SETTINGS
SCORE_LOCATIONS = [{"x": -240, "y": 280}, {"x": 240, "y": 280}]

# TIME SETTINGS
MAX_TIME = 300     # 5 minutes
TIME_LOCATION = {"x": 0, "y": 280}

class GameLogic():
    def __init__(self, screen, overlay):
        self.screen = screen
        self.overlay = overlay
        self.menu = False
        self.restart = False
        self.playing = False
        self.multiplayer = False
        self.timer = 0
        self.seconds_tracker = 0

    # def start_game(self):
    #     self.overlay.interrupt_pause()
    #     self.run_game()

    def restart_game(self): 
        self.overlay.interrupt_pause()
        self.restart = True

    def quit(self):
        self.overlay.interrupt_pause()
        self.running = False

    def setup_keypresses(self):
        # self.screen.onkeypress(self.start_game, "space")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.quit, "q")

    def reset_game_state(self):
        self.overlay.interrupt_pause()
        self.overlay.game_reset()
        self.timer = 0
        self.seconds_tracker = 0

    def body_collision_detection(self, snake, head):
        for segment in snake:
            if segment == head:
                continue
            if head.distance(segment) < 15:
                self.playing = False



# SINGLE PLAYER SETTINGS
SINGLEPLAYER_SNAKE_COLOUR = "black"
SINGLEPLAYER_SNAKE_LOCATION = {"x": -280, "y": 0}
SINGLEPLAYER_SCORE_LOCATION = {"x": 0, "y": 280}


class Singleplayer(GameLogic):
    def __init__(self, screen, overlay):
        super().__init__(screen, overlay)
        self.snake = Snake(SINGLEPLAYER_SNAKE_COLOUR, SINGLEPLAYER_SNAKE_LOCATION)
        self.score = Score(SINGLEPLAYER_SCORE_LOCATION)
        self.food = Food(self.screen.window_height())
        self.setup_keypresses()

    def setup_keypresses(self):
        super().setup_keypresses()
        self.screen.onkeypress(self.snake.left, "a")
        self.screen.onkeypress(self.snake.right, "d")
        self.screen.onkeypress(self.snake.down, "s")
        self.screen.onkeypress(self.snake.up, "w")
    
    def reset_game_state(self):
        super().reset_game_state()
        self.food.reset(self.screen.window_height())
        self.snake.reset()
        self.score.reset()
    
    def play_game(self):
        self.playing = True
        while self.playing:
            self.screen.update()
            if self.food.distance(self.snake.head) < 15:
                self.food.spawn_food()
                self.snake.append_segment()
                self.score.update_scoreboard()
            self.snake.move_snake()

            # Detect collision with wall
            x_pos, y_pos = self.snake.head.pos()
            if round(x_pos) > 280 or round(x_pos) < -280 or round(y_pos) > 280 or round(y_pos) < -280:
                self.playing = False

            # Detect Tail collision
            self.body_collision_detection(self.snake.segments, self.snake.head)

    def run_game(self):
        self.running = True
        while self.running:
            self.play_game()
            self.overlay.draw_gameover_text()
            if self.restart:
                self.reset_game_state()
                self.restart = False

class Multiplayer(GameLogic):
    def __init__(self, screen, overlay):
        super().__init__(screen, overlay)
        self.snakes = [Snake(SNAKE_COLOURS[0], SNAKE_LOCATIONS[0]), Snake(SNAKE_COLOURS[1], SNAKE_LOCATIONS[1])]
        self.scores = [Score(SCORE_LOCATIONS[0]), Score(SCORE_LOCATIONS[1])]
        self.time = Score(TIME_LOCATION)
        self.food = Food(self.screen.window_height())
        self.setup_keypresses()

    def setup_keypresses(self):
        super().setup_keypresses()
        self.screen.onkeypress(self.snakes[0].left, "a")
        self.screen.onkeypress(self.snakes[0].right, "d")
        self.screen.onkeypress(self.snakes[0].down, "s")
        self.screen.onkeypress(self.snakes[0].up, "w")
        self.screen.onkeypress(self.snakes[1].left, "Left")
        self.screen.onkeypress(self.snakes[1].right, "Right")
        self.screen.onkeypress(self.snakes[1].down, "Down")
        self.screen.onkeypress(self.snakes[1].up, "Up")

    def reset_game_state(self):
        super().reset_game_state()
        self.time.reset()
        self.food.reset(self.screen.window_height())
        for snake in self.snakes:
            snake.reset()
        for score in self.scores:
            score.reset()

    def play_game(self):
        self.playing = True
        self.timer = time.perf_counter()
        while self.playing:
            # update the timer
            self.seconds_tracker = time.perf_counter() - self.timer
            self.time.update_timer(MAX_TIME - self.seconds_tracker)
            # update screen with new time.
            self.screen.update()
            if self.seconds_tracker > MAX_TIME:
                break

            for i in range(len(self.snakes)):
                if self.food.distance(self.snakes[i].head) < 15:
                    self.food.spawn_food()
                    self.snakes[i].append_segment()
                    self.scores[i].update_scoreboard()
                self.snakes[i].move_snake()

                # Detect collision with wall
                x_pos, y_pos = self.snakes[i].head.pos()
                if round(x_pos) > 280 or round(x_pos) < -280 or round(y_pos) > 280 or round(y_pos) < -280:
                    self.playing = False

                # Detect Tail collision
                self.body_collision_detection(self.snakes[i].segments, self.snakes[i].head)

                # Detect collision with other snake
                self.body_collision_detection(self.snakes[i-1].segments, self.snakes[i].head)

    def run_game(self):
        self.running = True
        while self.running:
            self.play_game()
            self.overlay.draw_gameover_text()
            if self.restart:
                self.reset_game_state()
                self.restart = False

'''
Game Logic Class:
    - Attributes:
        - snake
        - food
        - walls
        - high_score
    - Methods:
        - check_wall_collision()
        - check_food_collision()
        - report() -> high score?
        - run_game()
'''