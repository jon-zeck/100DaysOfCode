# LINE SETTINGS
LINE_SHAPE = "square"
LINE_RESIZEMODE = "user"
LINE_COLOUR = "white"
NUM_MIDDLE_LINES = 60
MIDDLE_LINE_HEIGHT = 10
MIDDLE_LINE_WIDTH = 0.1

# SCREEN SETTINGS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = NUM_MIDDLE_LINES * MIDDLE_LINE_HEIGHT
SCREEN_BG_COLOUR = "black"
OFFSET = 50

# PADDLE SETTINGS
PADDLE_WIDTH_PX = 20
PADDLE_HEIGHT = 5
PADDLE_HEIGHT_PX = 20 * PADDLE_HEIGHT
PADDLE_WIDTH = 1
PADDLE_LOCATIONS_X_AXIS = [-(SCREEN_WIDTH-OFFSET) // 2 , (SCREEN_WIDTH-OFFSET-(PADDLE_WIDTH_PX * PADDLE_WIDTH)) // 2]
MOVE_CHUNK = 10

# BALL SETTINGS
BALL_SPEED = 10
SPEED = 0.1
MAX_SPEED = 0.05

# TEXT/SCORE SETTINGS
ALIGNMENT = "center"
SCORE_FONT = ("Arial", 30, "bold")
SET_MOVE_FALSE = False
SCORE_POS = [{"x":-200, "y": 250}, {"x":200, "y": 250}]