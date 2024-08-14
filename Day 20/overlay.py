from score import Text
import time

# TEXT OBJECT SETTINGS
GAME_OVER = "GAME OVER"
RESTART = "Press R to restart or Q to quit"
RESTART_TEXT_LOCATION = {"x":0, "y": -30}
START_TEXT = "PRESS ANY BUTTON TO START THE GAME"
TEXT_FLASH = .45

# 'Menu' Text
ONE_TWO_PLAYER_TEXT = "PRESS 1 FOR SINGLE PLAYER, PRESS 2 FOR MULTI PLAYER"
ONE_TWO_PLAYER_TEXT_LOCATION = {"x":0, "y": -40}

class Overlay():
    def __init__(self, screen):
        self.screen = screen
        self.pause = False
        self.menu = False
        self.restart_text = Text(RESTART, RESTART_TEXT_LOCATION)
        self.game_over_text = Text(GAME_OVER)
        self.start_text = Text(START_TEXT)
        self.one_two_player_text = Text(ONE_TWO_PLAYER_TEXT, ONE_TWO_PLAYER_TEXT_LOCATION)
    
    def pause_game(self, text, flashing=False):
        self.pause = True
        while self.pause:
            text.write_text()
            self.screen.update()
            time.sleep(TEXT_FLASH)
            text.clear()
            if flashing:
                self.screen.update()
                time.sleep(TEXT_FLASH)

    def interrupt_pause(self):
        self.pause = False

    def draw_menu(self):
        self.pause_game(self.one_two_player_text, False)

    def draw_gameover_text(self):
        self.game_over_text.write_text()
        self.pause_game(self.restart_text, True)

    def game_reset(self):
        self.game_over_text.clear()


'''
    What is a Menu?
    What can it do?
    Does it store settings?


    Tickbox for selecting between 1 and 2 players.
        Default is 1.
        If 2 is selected, 1 is deselected and vice versa.
    Button for playing the game.

    Option for game speed.
    Option for picking snake colours.
    Option for time limit.
'''