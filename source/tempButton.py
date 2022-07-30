#!/usr/bin/python3

from sense_hat import SenseHat,ACTION_PRESSED,ACTION_HELD,ACTION_RELEASED
from time import sleep

sense = SenseHat()
sense.clear()

#functions
def measureTemp():
    temperature1 = round(sense.get_temperature_from_pressure(),2)
    #temperature2 = round(sense.get_temperature(),2)
    #return (temperature1 + temperature2)/2
    return temperature1

def show_temp(vel):
    temp1 = measureTemp()
    tempStr = str(temp1)
    if temp1 <= 21.0:
        sense.show_message(tempStr,scroll_speed=vel,text_colour=(0,128,255),back_colour=(0,0,0))
    elif temp1 > 21.0  and temp1 <= 25:
        sense.show_message(tempStr,scroll_speed=vel,text_colour=(0,153,0),back_colour=(0,0,0))
    elif temp1 > 25:
        sense.show_message(tempStr,scroll_speed=vel,text_colour=(153,0,0),back_colour=(0,0,0))
    print(temp1)

def press_down(event):
    if event.action == 'pressed' and event.direction == 'down':
        return show_temp(0.1)

def main():
    try:
        while True:
            # event = sense.stick.wait_for_event(emptybuffer = True)
            # print('the joystick was {} {}'.format(event.action,event.direction))
            sense.stick.direction_down = press_down
            sleep(0.05) # This is to avoid CPU excess
    except KeyboardInterrupt:
            # This keyboard interruption allows us to stop the game by using control-c
            # and clears the leds switching them off
            sense.clear()
            print('\n Stopped')

# Run this program
main()