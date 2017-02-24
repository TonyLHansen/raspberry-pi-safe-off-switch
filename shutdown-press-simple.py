#!/usr/bin/env python3
from gpiozero import Button
import os
Button(21).wait_for_press()
os.system("sudo poweroff")
