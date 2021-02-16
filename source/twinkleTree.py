from sense_hat import SenseHat
from time import sleep
import random

# Function to make RGB coloring random
def random_color():
    color_range = list(range(256))
    red = random.choice(color_range)
    green = random.choice(color_range)
    blue = random.choice(color_range)
    return [red,green,blue]

sense = SenseHat()

sense.clear()

X = [0, 100, 0] # Green
O = [0, 0, 0] # Empty
B = [139, 69, 19] # Brown

try:
    while True:
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
        sense.set_pixels(xmas_tree) 
        sleep(2)
except KeyboardInterrupt:
    sense.clear()
    print('\n Stopped')
