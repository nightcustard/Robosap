# by Augustus Nightcustard
# heavily based upon work by Carl Monk (@ForToffee)
# based on work from http://playground.arduino.cc/Main/RoboSapienIR
# command codes originally from http://www.aibohack.com/robosap/ir_codes.htm

import robo
import time

rs=robo.Robo(21)	#create Robo object for GPIO 21
rs.send_code(0xB1)	#Issue wakeup command
time.sleep(10)
rs.send_code(0x81)	#Right arm up
time.sleep(1)
rs.send_code(0x81)
time.sleep(1)
rs.send_code(0x82)	#Right wrist out
time.sleep(1)
rs.send_code(0x85)	#Right wrist in
time.sleep(1)
rs.send_code(0x82)      #
time.sleep(1)
rs.send_code(0x85)      #
time.sleep(1)
rs.send_code(0x86)      # walk fwd
time.sleep(1)
rs.send_code(0x86)      # walk fwd

rs.send_code(0x86)      # walk fwd
time.sleep(1)
rs.send_code(0xA0)      #RightTurnStep
time.sleep(2)
rs.send_code(0xA0)      #RightTurnStep
time.sleep(2)
rs.send_code(0xC0)      #RHStrike3
time.sleep(1)
rs.send_code(0xC2)      #Burp
time.sleep(1)
rs.send_code(0xC3)      #RHStrike3
time.sleep(1)
rs.send_code(0xC3)
time.sleep(1)
# raw_input('Enter')
rs.send_code(0x89)	#Left arm up
time.sleep(2)
rs.send_code(0x89)
for i in range(0,2):
	rs.send_code(0x8B)	#Tilt left
	time.sleep(1)
	rs.send_code(0x83)	#Tilt right	
	time.sleep(1)
	rs.send_code(0x83)
	time.sleep(1)
	rs.send_code(0x8B)
	time.sleep(1)
rs.send_code(0x8C)	#Left arm down
rs.send_code(0x84)	#Right arm down
time.sleep(1)
rs.send_code(0x8C)
time.sleep(1)
rs.send_code(0x84)
time.sleep(1)
# raw_input('Enter')
rs.send_code(0xC4)	#Hi 5
time.sleep(1)
# raw_input('Enter')
rs.send_code(0xCE)	#Roar
# rs.send_code(0xD1)      # Rosebud
