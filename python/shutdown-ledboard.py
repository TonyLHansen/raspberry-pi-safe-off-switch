#!/usr/bin/env python3
from gpiozero import Button, LEDBoard
from signal import pause
import warnings, os, sys

offGPIO = int(sys.argv[1]) if len(sys.argv) >= 2 else 21
offtime = int(sys.argv[2]) if len(sys.argv) >= 3 else 6
mintime = 1       # notice switch after mintime seconds
actledGPIO = 47   # activity LED
powerledGPIO = 35 # power LED

def shutdown(b):
    # find how long the button has been held
    p = b.pressed_time
    # blink rate will increase the longer we hold
    # the button down. E.g., at 2 seconds, use 1/4 second rate.
    leds.blink(on_time=0.5/p, off_time=0.5/p)
    if p > offtime:
        os.system("sudo poweroff")

def when_pressed():
    # start blinking with 1/2 second rate
    leds.blink(on_time=0.5, off_time=0.5)

def when_released():
    # be sure to turn the LEDs off if we release early
    leds.off()

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    leds = LEDBoard(actledGPIO, powerledGPIO)

btn = Button(offGPIO, hold_time=mintime, hold_repeat=True)
btn.when_held = shutdown
btn.when_pressed = when_pressed
btn.when_released = when_released
pause()
