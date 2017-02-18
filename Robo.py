# by Augustus Nightcustard
# github.com/nightcustard/Robosap
# heavily based upon work by Carl Monk (@ForToffee)
# based on work from http://playground.arduino.cc/Main/RoboSapienIR
# command codes originally from http://www.aibohack.com/robosap/ir_codes.htm

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

CODE_RSTurnRight       = 0x80
CODE_RSRightArmUp      = 0x81
CODE_RSRightArmOut     = 0x82
CODE_RSTiltBodyRight   = 0x83
CODE_RSRightArmDown    = 0x84
CODE_RSRightArmIn      = 0x85
CODE_RSWalkForward     = 0x86
CODE_RSWalkBackward    = 0x87
CODE_RSTurnLeft        = 0x88
CODE_RSLeftArmUp       = 0x89
CODE_RSLeftArmOut      = 0x8A
CODE_RSTiltBodyLeft    = 0x8B
CODE_RSLeftArmDown     = 0x8C
CODE_RSLeftArmIn       = 0x8D
CODE_RSStop            = 0x8E
# CODE_RSMtrCmd	       = 0x90
# CODE_RSProgPlay        = 0x91
# CODE_RSRightSensProg   = 0x92
# CODE_RSLeftSensProg    = 0x93
# CODE_RSSonicProg       = 0x94
CODE_RSRightTurnStep   = 0xA0
CODE_RSRHThump         = 0xA1
CODE_RSRHThrow         = 0xA2
CODE_RSSleep           = 0xA3
CODE_RSRHPickup        = 0xA4
CODE_RSLeanBackward    = 0xA5
CODE_RSFwdStep         = 0xA6
CODE_RSBackwardStep    = 0xA7
CODE_RSLeftTurnStep    = 0xA8
CODE_RSLHThump         = 0xA9
CODE_RSLHThrow         = 0xAA
CODE_RSListen          = 0xAB
CODE_RSLHPickup        = 0xAC
CODE_RSLeanFwd         = 0xAD
CODE_RSReset           = 0xAE
#  CODE_RSMstrCmdProgExe  = 0xB0
CODE_RSWakeUp          = 0xB1
# CODE_RSRightSensPrgExe = 0xB2
# CODE_RSLeftSensPrgExe  = 0xB3
# CODE_RSSonicSensPrgExe = 0xB4
CODE_RSRightHandStrike = 0xC0
CODE_RSRHSweep         = 0xC1
CODE_RSBurp            = 0xC2
CODE_RSRHStrike2       = 0xC3
CODE_RSHigh5           = 0xC4
CODE_RSRHStrike1       = 0xC5
CODE_RSBulldozer       = 0xC6
CODE_RSTrump           = 0xC7
CODE_RSLHStrike3       = 0xC8
CODE_RSLHSweep         = 0xC9
CODE_RSWhistle         = 0xCA
CODE_RSLHStrike2       = 0xCB
CODE_RSTalkBack        = 0xCC
CODE_RSLHStrike1       = 0xCD
CODE_RSRoar            = 0xCE
CODE_RSAllDemo         = 0xD0
CODE_RSPowerOff        = 0xD1
CODE_RSKarateDemo      = 0xD2
CODE_RSRudeDemo        = 0xD3
CODE_RSDance           = 0xD4
CODE_RSKarateChop      = 0xD6
CODE_RSNoOp            = 0xEF
CODE_RSFeetShuffle     = 0xF6
CODE_RSRaiseArmThrow   = 0xFC

CYCLE = 833

class Robo(object):

	def __init__(self, pin):
		self.pin = pin
		self.pi = pigpio.pi() # Connect to Pi.
		self.pi.set_mode(pin, pigpio.OUTPUT) # IR TX connected to this GPIO.
		self.pi.write(self.pin, 1)
		self.pi.wave_clear()
		
		self.wf_head = self.add_wave(8, 8)
		self.wf_hi = self.add_wave(4, 1)
		self.wf_lo = self.add_wave(1, 1)
		self.wf_tail = self.add_wave(8, 8)
		
		self.keep_alive = self.create_code(CODE_RSNoOp)


	def add_wave(self, hi, lo):
		self.pi.wave_add_generic([pigpio.pulse(1<<self.pin, 0, hi * CYCLE), pigpio.pulse(0, 1<<self.pin, lo * CYCLE)])
		return self.pi.wave_create()
	
	def create_code(self, code):
		data = code
		print data
		wave = []
		wave.append(self.wf_head)

		for x in range(8):
			if (data & 128 != 0):
				wave.append(self.wf_hi)
				print 1
			else:
				wave.append(self.wf_lo)
				print 0
			data <<= 1

		wave.append(self.wf_tail)
		print wave
		print "end"
		return wave

	def send_wave(self, wave):
		#print wave
		self.pi.wave_chain(wave)
		while self.pi.wave_tx_busy():
			time.sleep(0.002)

		self.pi.write(self.pin, 1)
	
	def send_code(self, code):
		self.send_wave(self.create_code(code))
		time.sleep(0.5)

	def clean_up(self):
		pi.wave_clear()
pi.stop() # Disconnect from Pi.
