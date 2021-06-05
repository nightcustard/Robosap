#!/usr/bin/python
# volumeHIGH.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
# print "Volume High"
GPIO.output(18,GPIO.HIGH)

