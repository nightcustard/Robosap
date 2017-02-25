#!/usr/bin/python

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
#raw_input("Press Enter when ready\n>")
#print "Waiting for falling edge on GPIO 12"

try:
    GPIO.wait_for_edge(12, GPIO.FALLING)
    #print "\nFalling edge detected. Going for shutdown"
    #Use falling edge detection to see if pin is pulled 
    #low to avoid repeated polling
    os.system("sudo shutdown -h now")
    #Send command to system to shutdown
except KeyboardInterrupt:
    #print "Process interrupted, closing"
    GPIO.cleanup()  #clean up GPIO on CTRL+C exit
GPIO.cleanup()
#Revert all GPIO pins to their normal states (i.e. input = safe)
