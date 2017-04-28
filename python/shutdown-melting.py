#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import pygame.mixer
from pygame.mixer import Sound
import time, os

holdTime = 10
offGPIO = 21

pygame.mixer.init()
melting = Sound("ImMeltingMelting.ogg")
nohome = Sound("NoPlaceLikeHome.ogg")

def shutdown():
    # stop playing one sound and switch to another
    melting.stop()
    nohome.play()
    # give it a chance to play
    time.sleep(1)
    # and shutdown for real
    os.system("sudo poweroff")

def when_pressed():
    # start playing
    melting.play(loops=holdTime/melting.get_length())

def when_released():
    # stop playing if released early
    melting.stop()

btn = Button(offGPIO, hold_time=holdTime)
btn.when_held = shutdown
btn.when_pressed = when_pressed
btn.when_released = when_released
pause()
