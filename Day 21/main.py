''' Day 21: Pong Game '''

from turtle import Screen, Turtle
from globals import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BG_COLOUR, PADDLE_LOCATIONS_X_AXIS
from game import Game

if __name__ == '__main__':
    # start the game.
    # 1. Create the Screen
    # 2. Create a moving paddle
    # 3. Create another paddle
    # 4. Create the moving ball
    # 5. Detect collision with wall and bounce
    # 6. Detect collision with paddle
    # 7. Detect a miss
    # 8. Keep 
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, startx=None, starty=None)
    screen.bgcolor(SCREEN_BG_COLOUR)
    screen.title("Pong")

    # DEBUG DRAW BOUNDARY LINES
    turtle1 = Turtle()
    turtle1.hideturtle()
    turtle1.speed("fastest")
    turtle1.color("orange")
    turtle1.penup()
    turtle1.setpos(PADDLE_LOCATIONS_X_AXIS[0] + 10, -300)
    turtle1.pendown()
    turtle1.setpos(PADDLE_LOCATIONS_X_AXIS[0] + 10, 300)

    turtle2 = Turtle()
    turtle2.hideturtle()
    turtle2.speed("fastest")
    turtle2.color("red")
    turtle2.penup()
    turtle2.setpos(PADDLE_LOCATIONS_X_AXIS[0], -300)
    turtle2.pendown()
    turtle2.setpos(PADDLE_LOCATIONS_X_AXIS[0], 300)

    turtle3 = Turtle()
    turtle3.hideturtle()
    turtle3.speed("fastest")
    turtle3.color("orange")
    turtle3.penup()
    turtle3.setpos(PADDLE_LOCATIONS_X_AXIS[1] - 10, -300)
    turtle3.pendown()
    turtle3.setpos(PADDLE_LOCATIONS_X_AXIS[1] - 10, 300)

    turtle4 = Turtle()
    turtle4.hideturtle()
    turtle4.speed("fastest")
    turtle4.color("red")
    turtle4.penup()
    turtle4.setpos(PADDLE_LOCATIONS_X_AXIS[1], -300)
    turtle4.pendown()
    turtle4.setpos(PADDLE_LOCATIONS_X_AXIS[1], 300)

    screen.delay(0)

    game = Game(screen)

    screen.listen()

    game.play()

'''
What the game needs:
1. Class for paddle.
2. Class for ball.
3. Class for Score.
4. Class for middle lines - although they look like paddles, so much they can both extend the turtles class.

The ball also needs to do continuous checks to make sure it does not move out of bounds. I.e. reverse movement upon collision.


General game loop is:
1. Check if Ball has made contact with a wall.
1a. If yes, reverse velocity along the y-axis.
1b. If no, keep moving.

2. Check if Ball has made contact with a paddle.
2a. If yes, reverse velocity along the x-axis.
2b. If no, keep moving.

3. Check if Ball has gone past player #1.
3a. If yes, increase score of player #2.
3b. Did the player win?
3bi. if yes, end game.
3bii. if no, restart play.

4. Check if Ball has gone past player #2.
4a. If yes, increase score of player #1.
4b. Did the player win?
4bi. if yes, end game.
4bi. if no, restart play.

5. Move ball.

6. First to x amount of points wins.
'''