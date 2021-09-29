# from sense_hat import SenseHat

# This sentence active to activate the Sense Hat emulator
from sense_emu import SenseHat
from time import sleep
import random

# Function to make RGB coloring random
def random_color():
    '''
    Function to generate random RGB colouring. 
    It takes a random number from 0 to 256 for each of the Red Green Blue options and returns a list to mix the three.
    The result is one of the possible RGB colors available. 
    '''
    color_range = list(range(256))      # Range of colors
    red = random.choice(color_range)    # Choice for red
    green = random.choice(color_range)  # Choice for green
    blue = random.choice(color_range)   # Choice for blue
    return [red,green,blue]             # Returned color as RGB, mix of the three choices

# We create the sense object to work with it.
sense = SenseHat()

# If there's anything in the matrix we clear it
sense.clear()

# Definition of common colors to be used. 
# Green for the pine needles, brown for the timber and no color. 
X = [0, 100, 0] # Green
O = [0, 0, 0] # Empty
B = [139, 69, 19] # Brown

# It's going to run for a while and the tree lights will keep changing.
# We use an infinite loop while True. 
try:
    while True:
        # Some squares will stay off: 0
        # Some squares will change: random_color()
        # Some squares will keep green: X
        # Some squares will stay brown: B
        xmas_tree= [
	        O, O, O, random_color(), X, O, O, O,
	        O, O, X, X, X, random_color(), O, O,
	        O, random_color(), X, X, random_color(), X, X, O,
	        O, O, X, random_color(), X, X, O, O,
	        O, X, random_color(), X, X, random_color(), X, O,
	        X, random_color(), X, random_color(), X, X, random_color(), X,
	        O, O, O, B, B, O, O, O,
	        O, O, O, B, B, O, O, O
	        ]
        # We apply the color configuration to the matrix in the sense hat
        sense.set_pixels(xmas_tree)
        # the ones with random_color() wil change every 2 seconds 
        sleep(2)
except KeyboardInterrupt:   #This exception allows for control-C kill but it also clears the matrix. 
    sense.clear()
    print('\n Stopped')


