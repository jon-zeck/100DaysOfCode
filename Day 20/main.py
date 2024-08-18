from gameLogic import GameLogic, Singleplayer, Multiplayer
from turtle import Screen
from overlay import Overlay


# SCREEN SETTINGS
BG_COLOUR = "orange"
GAME_SCREEN = 600
GAME_TITLE = "Snake Game"
TRACER_OFF = 0

class Start():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(GAME_SCREEN, GAME_SCREEN)
        self.screen.bgcolor(BG_COLOUR)
        self.screen.title(GAME_TITLE)
        self.screen.tracer(TRACER_OFF)
        self.screen.listen()
        self.screen.onkeypress(self.select_player_one, "1")
        self.screen.onkeypress(self.select_player_two, "2")
        self.overlay = Overlay(self.screen)
        self.menu = False
        self.multiplayer = False

    def select_player_one(self):
        if not self.menu:
            return
        self.overlay.interrupt_pause()
        self.menu = False
        self.multiplayer = False

    def select_player_two(self):
        if not self.menu:
            return
        self.overlay.interrupt_pause()
        self.menu = False
        self.multiplayer = True

    def start(self):
        self.menu = True
        self.overlay.draw_menu()
        if self.multiplayer:
            game = Multiplayer(self.screen, self.overlay)
        else:
            game = Singleplayer(self.screen, self.overlay)
        game.run_game()

if __name__ == "__main__":
    screen = Screen()
    screen.setup(GAME_SCREEN, GAME_SCREEN)
    screen.bgcolor(BG_COLOUR)
    screen.title(GAME_TITLE)
    screen.tracer(TRACER_OFF)
    screen.listen()

    start = Start()

    start.start()
    
    # game = GameLogic(screen)
    # game.start()


'''
    FURTHER IDEAS:
    1. Create timer - game lasts 5 minutes in multiplayer
    2. Spawn multiple pieces of food, one every 10 turns or so.
    3. Give each snake 10 moves of invulnerability from other snakes.
    4. Each time a snake dies in multiplayer, its score is divided by 2
'''

'''
What classes exist?
    - What do they have?
    - What can they do?

Snake class:
    - Attributes:
        - head
        - segments
    - Methods:
        - grow()
        - die()
        - report() -> length
        - move()
        - change_angle()
'''
