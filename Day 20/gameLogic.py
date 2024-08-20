from food import Food
from snake import Snake
from score import Score
from globals import SINGLEPLAYER_SCORE_LOCATION, SINGLEPLAYER_SNAKE_COLOUR, SINGLEPLAYER_SNAKE_LOCATION, SNAKE_COLOURS, SNAKE_LOCATIONS, SCORE_LOCATIONS, TIME_LOCATION, MAX_TIME, FOOD_SPAWNRATE
import time

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

    def restart_game(self): 
        self.overlay.interrupt_pause()
        self.restart = True

    def quit(self):
        self.overlay.interrupt_pause()
        self.running = False

    def setup_keypresses(self):
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.quit, "q")

    def reset_game_state(self):
        self.overlay.interrupt_pause()
        self.overlay.game_reset()
        self.timer = 0
        self.seconds_tracker = 0

    def body_collision_detection(self, snake, head):
        collision = False
        for segment in snake[1:]:
            if head.distance(segment) < 15:
                collision = True
        return collision


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
        self.food.reset()
        self.food = Food(self.screen.window_height())
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
            if self.body_collision_detection(self.snake.segments, self.snake.head) == True:
                self.playing = False

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
        self.foods = [Food(self.screen.window_height())]
        self.food_clock = 0
        self.dead = [False, False]
        self.invulnerability = [False, False]
        self.invulnerability_counter = [0, 0]
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
        for food in self.foods:
            food.reset()
        for _ in range(len(self.foods)):
            self.foods.pop()
        self.foods.append(Food(self.screen.window_height()))
        for snake in self.snakes:
            snake.reset()
        for score in self.scores:
            score.reset()
        self.food_clock = 0
        

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
            
            if self.food_clock % FOOD_SPAWNRATE == 0:
                self.foods.append(Food(self.screen.window_height()))
            for i in range(len(self.snakes)):
                # CHECK FOOD COLLISIONS
                for food in self.foods:
                    if food.distance(self.snakes[i].head) < 15:
                        food.reset()
                        self.foods.remove(food)
                        self.snakes[i].append_segment()
                        self.scores[i].update_scoreboard()

                # CHECK WALL COLLISION
                x_pos, y_pos = self.snakes[i].head.pos()
                if round(x_pos) > 280 or round(x_pos) < -280 or round(y_pos) > 280 or round(y_pos) < -280:
                    self.dead[i] = True

                if self.invulnerability[i] and self.invulnerability_counter[i] < 10:
                    self.invulnerability_counter[i] += 1
                    continue
                if self.invulnerability[i]:
                    self.invulnerability[i] = False
                    self.invulnerability_counter[i] = 0

                # CHECK OWN TAIL COLLISION
                if not self.dead[i] and not self.invulnerability[i]:
                    self.dead[i] = self.body_collision_detection(self.snakes[i].segments, self.snakes[i].head)

                # CHECK OTHER SNAKE COLLISION
                if not self.dead[i] and not self.invulnerability[i]:
                    self.dead[i] = self.body_collision_detection(self.snakes[i-1].segments, self.snakes[i].head)

                self.food_clock += 1
            
            # check if collision has occured.
            #   if yes, need to reset snake but let the game continue.
            for i in range(len(self.snakes)):
                if self.dead[i]:
                    self.snakes[i].reset()
                    self.scores[i].half_score()
                    self.dead[i] = False
                    self.invulnerability[i] = True
                    self.invulnerability_counter[i] = 0
                else:
                    # move the snake
                    self.snakes[i].move_snake()


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