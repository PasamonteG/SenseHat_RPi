# Copied this program from https://projects.raspberrypi.org/en/projects/sense-hat-pong
# I intend to modify it and make it a little bit more functional
# Suggestions welcome

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

# Variables
white = [255,255,255]
blue = [77,136,255]
bat_y = 4
ball_position = [2,3]
ball_velocity = [1,1]

# Functions 
def draw_bat():
    sense.set_pixel(0,bat_y,white)
    sense.set_pixel(0,bat_y+1,white)
    sense.set_pixel(0,bat_y-1,white)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1

def draw_ball():
    global ball_position,ball_velocity
    sense.set_pixel(ball_position[0],ball_position[1],blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] >= 7 or ball_position[0] <= 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] >= 7 or ball_position[1] <= 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y -1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 0:
        sense.clear(0,0,0)
        sense.show_message('Lose',text_colour=(100,60,20),back_colour=(0,0,0))
        sense.clear()
        go = False

# Main program
try:
    go = True
    while go == True:
        go = True
        sense.stick.direction_up = move_up
        sense.stick.direction_down = move_down
        sense.clear(0,0,0)
        draw_bat()
        draw_ball()
        sleep(0.3)
except KeyboardInterrupt:
    # This keyboard interruption allows us to stop the game by using control-c 
    # and clears the leds switching them off
    sense.clear()
    print('\n Stopped')
    