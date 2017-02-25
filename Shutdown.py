#!/usr/bin/python
# This file is intended to be autorun on boot using systemd

import sys
sys.path.insert(0,"/home/pi/")
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
#BCM selects GPIO numbering,BOARD selects pin numbering

GPIO.setup(12, GPIO.IN)
#In this case, no pull up/down is needed as the input is either 3v3 or 0v
#GPIO 12 is connected to VRE on the Robosap motherboard which changes from 3v3
#to 0v when 'Rosebud' sleep is executed.

try:
    GPIO.wait_for_edge(12, GPIO.FALLING)
    #Use falling edge detection to see if pin is pulled 
    #low to avoid repeated polling
    os.system("sudo shutdown -h now")
    #Send command to system to shutdown
except:
    GPIO.cleanup()  #clean up GPIO on error
GPIO.cleanup()
#Revert all GPIO pins to their normal states (i.e. input = safe)
