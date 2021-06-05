#!/usr/bin/python
# quiet.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#print "Volume Low"
GPIO.output(18,GPIO.LOW)
