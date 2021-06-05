#!/usr/bin/python3
# coding=utf-8

# RC.py (Robosapien Commander)
# heavily based upon work by Carl Monk (@ForToffee)
# based on work from http://playground.arduino.cc/Main/RoboSapienIR
# command codes originally from http://www.aibohack.com/robosap/ir_codes.htm

import sys
import time
#import RPi.GPIO as GPIO
import datetime
import os
import subprocess
import robo

sys.path.insert(0,"/home/pi/")

rs=robo.Robo(21)      	# Create Robo object for GPIO 21

# Tuple is indexed 0 to 65 ( in this case)
# Robosapien remote command codes

remote = (0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x90, 0x91, 0x92, 0x93, 0x94, 0x98, 0x9A, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD6, 0xF6, 0xFB, 0xFC)

# 'command' tuple.  Contains the designated remote command text followed by the index of the associated remote command parameters contained in the 'remote' tuple
# Commands must be in same order as the menu below and can be moved (as a pair - text and index number) to suit menu order. Can substitute any text for placeholder text (eg) "WII-2on" can be "lights on"

command = ("turn right", 0, "right arm up", 1, "right arm out", 2, "tilt body right", 3, "right arm down", 4, "right arm in", 5, "walk forward", 6, "walk backward", 7, "turn left", 8, "left arm up", 9, "left arm out", 10, "tilt body left", 11, "left arm down", 12, "left arm in", 13, "stop", 14, "master command programme", 15, "programme play", 16, "right sensor programme", 17, "left sensor programme", 18, "sonic sensor programme", 19, "quiet execute", 20, "quiet execute with subs", 21, "right turn step", 22, "right hand thump", 23, "right hand throw", 24, "sleep", 25, "right hand pickup", 26, "lean backward", 27, "forward step", 28, "backward step", 29, "left turn step", 30, "left hand thump", 31, "left hand throw", 32, "listen", 33, "left hand pickup", 34, "lean forward", 35, "reset", 36, "execute", 37, "wakeup", 38, "right sensor prog exec", 39, "left sensor prog exec", 40, "sonic sensor prog exec", 41, "right hand strike 3", 42, "right hand sweep", 43, "burp", 44, "right hand strike 2", 45, "high 5", 46, "right hand strike 1", 47, "bulldozer", 48, "fart", 49, "left hand strike 3", 50,  "left hand sweep", 51, "whistle", 52, "left hand strike 2", 53, "talkback", 54, "left hand strike 1", 55, "roar", 56, "all demo", 57, "power off", 58, "demo 1", 59, "demo 2", 60, "dance", 61, "karate chop", 62, "feet shuffle", 63, "no-op", 64, "raise arm throw", 65) 

# This section looks for one or more command line arguments and executes each in turn, thus permitting multiple commands to be executed at the same time

if len(sys.argv) >= 2: # Check for one or more command line arguments, if none go to menu section below. 
	n = len(sys.argv)-1 # n = number of command line arguments
	for x in range(n): # x runs from 0 to n-1
		G = sys.argv[x+1] #[0] is /home/pi/Projects/Robosap/RC.py; [1] is (eg) turn right; [2] is second command line argument etc.
		print (G)
		try:                         # allows errors to be handled
			index = command.index(G) # return the index of the text in the command tuple, if it isn't there, then:
		except ValueError:           # a ValueError is returned if the input isn't in the command tuple
			print('\033[1;31;40mInput not recognised, please try again.\n')  #see end for explanation of ANSI escape sequence
#			help()
			exit()

		i = command[index+1]  # i is the index position of the remote command code in the 'remote' tuple
#		print('\033[1;32;40mTurning', G, '\n')
		c = remote[i]
#		print('index = ', i, 'remote = ', c)
		rs.send_code(c)
	exit()	
		
# This is the text prompt menu section if no command line arguments were entered
else:
	
	print("\n\033[1;36;40mWelcome to Pi Robosapien\n")
	print("\n\033[1;36;40mPlease enter the number corresponding to what you want to do.\n")
	print("\033[1;36;40mEnter 1 to turn right.")
	print("\033[1;36;40mEnter 2 to move right arm up.")
	print("\033[1;36;40mEnter 3 to move right arm out.")
	print("\033[1;36;40mEnter 4 to tilt body right.")
	print("\033[1;36;40mEnter 5 to move right arm down.")
	print("\033[1;36;40mEnter 6 to tuck right arm in.") 
	print("\033[1;36;40mEnter 7 to walk forward.")
	print("\033[1;36;40mEnter 8 to walk backward.")
	print("\033[1;36;40mEnter 9 to turn left.")
	print("\033[1;36;40mEnter 10 to move left arm up.")
	print("\033[1;36;40mEnter 11 to stick left arm out.")
	print("\033[1;36;40mEnter 12 to tilt body left.")
	print("\033[1;36;40mEnter 13 to move left arm down.")
	print("\033[1;36;40mEnter 14 to tuck left arm in.")
	print("\033[1;36;40mEnter 15 to stop.")
	print("\033[1;36;40mEnter 16 to build master command programme.")
	print("\033[1;36;40mEnter 17 to play programme.")
	print("\033[1;36;40mEnter 18 to build right sensor programme.")
	print("\033[1;36;40mEnter 19 to build left sensor programme.")
	print("\033[1;36;40mEnter 20 to build sonic sensor programme.")
	print("\033[1;36;40mEnter 21 to quiet execute.")
	print("\033[1;36;40mEnter 22 to quiet execute with subs.")
	print("\033[1;36;40mEnter 23 to right turn step.")
	print("\033[1;36;40mEnter 24 to right hand thump.")
	print("\033[1;36;40mEnter 25 to right hand throw.")
	print("\033[1;36;40mEnter 26 to sleep.")
	print("\033[1;36;40mEnter 27 to right hand pickup.")
	print("\033[1;36;40mEnter 28 to lean backward.")
	print("\033[1;36;40mEnter 29 to forward step.")
	print("\033[1;36;40mEnter 30 to backward step.")
	print("\033[1;36;40mEnter 31 to left turn step.")
	print("\033[1;36;40mEnter 32 to left hand thump.")
	print("\033[1;36;40mEnter 33 to left hand throw.")
	print("\033[1;36;40mEnter 34 to listen.")
	print("\033[1;36;40mEnter 35 to left hand pickup.")
	print("\033[1;36;40mEnter 36 to lean forward.")
	print("\033[1;36;40mEnter 37 to reset.")
	print("\033[1;36;40mEnter 38 to execute.")
	print("\033[1;36;40mEnter 39 to wakeup.")
	print("\033[1;36;40mEnter 40 to execute right sensor prog.")
	print("\033[1;36;40mEnter 41 to execute left sensor prog.")
	print("\033[1;36;40mEnter 42 to execute sonic sensor prog.")
	print("\033[1;36;40mEnter 43 to right hand strike 3.")
	print("\033[1;36;40mEnter 44 to right hand strike 3.")
	print("\033[1;36;40mEnter 45 to burp.")
	print("\033[1;36;40mEnter 46 to right hand strike 2.")
	print("\033[1;36;40mEnter 47 to high five.")
	print("\033[1;36;40mEnter 48 to right hand strike 1.")
	print("\033[1;36;40mEnter 49 to bulldozer.")
	print("\033[1;36;40mEnter 50 to fart.")
	print("\033[1;36;40mEnter 51 to left hand strike 3.")
	print("\033[1;36;40mEnter 52 to left hand sweep.")
	print("\033[1;36;40mEnter 53 to whistle.")
	print("\033[1;36;40mEnter 54 to left hand strike 2.")
	print("\033[1;36;40mEnter 55 to talkback.")
	print("\033[1;36;40mEnter 56 to left hand strike 1.")
	print("\033[1;36;40mEnter 57 to roar.")
	print("\033[1;36;40mEnter 58 to start all demo.")
	print("\033[1;36;40mEnter 59 to power off (Rosebud).")
	print("\033[1;36;40mEnter 60 to perform demo 1.")
	print("\033[1;36;40mEnter 61 to perform demo 2.")
	print("\033[1;36;40mEnter 62 to dance.")
	print("\033[1;36;40mEnter 63 to karate chop.")
	print("\033[1;36;40mEnter 64 to feet shuffle.")
	print("\033[1;36;40mEnter 65 to do nothing (no-op).")
	print("\033[1;36;40mEnter 66 to raise arm throw.")
	print("\033[1;36;40mEnter any other key or number to quit.\n")

	b = 1
	n = 66  # when adding more commands, n is the number of commands
	while (b > 0) and (b < n+1):  
		try:
			b = int(input("\033[0;37;40mWhat would you like to do? \033[0K"))  # \033[0K = erase to end of line
			print("\r\033[1A\033[1A")  # \r = move to beginning of line (&LF?); \033[1A = move up one line https://stackoverflow.com/questions/11283625/overwrite-last-line-on-terminal
		except ValueError:
			print('\033[1;31;40mTerminating')
			break
		if (b <= 0) or (b > n):  # when adding more commands, n in (b > n) is the number of commands
			break
		else:
			inp = b-2
			B = b+inp
			G = command[B]  # Tells the print command below what the command is (eg) "fairy lights off"
			index = command.index(G) # Gives the index number of the command in the command tuple
			i = command[index+1]  # i is the start index position of the five remote control codes in the 'remote' tuple
			c = remote[i]   
			rs.send_code(c)

exit()

#Troubleshooting:
#print('Index of G:', index)
#print('remote[i]', remote[i])
#print('remote[i+1]', remote[i+1])
#print('remote[i+2]', remote[i+2])
#print('remote[i+3]', remote[i+3])
#print('remote[i+4]', remote[i+4])
