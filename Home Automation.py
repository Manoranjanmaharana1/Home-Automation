# Home Automation System : This system detects whether a person has entered into the room or not, or any command has been
# 			   provided or not. When a person enters the room, the IR sensor detects his/her entry and accordingly
#			   switches on the light. 

import RPi.GPIO as gpio
import time
from pushbullet import Pushbullet



pb = Pushbullet("o.vGrPgqzm2rxUzcrnvyZuSbHrr9nYeD8z")
gpio.setmode(gpio.BOARD)		
gpio.setup(16, gpio.IN)			#input from IR sensor
gpio.setup(40, gpio.OUT)		#output to electric bulb
gpio.setwarnings(False)
time.sleep(1.5)
try:
	entered = False
	while True:
		time.sleep(1)
		pushes = pb.get_pushes()
		if ('body' in pushes[0].keys()):
			msg2 = pushes[0]['body']			#getting user command
		msg1 = gpio.input(16)					#waiting for any motion
		print(msg1)
		if msg1 == True or msg2 == 'On': 
			entered = True
			msg2 = 'On'
			print('Turning Lights On')
			pb.push_note("Home Automation System","Light is On!!")
			gpio.output(40, 0)
		while(entered):
			time.sleep(0.5)
			pushes = pb.get_pushes()
			if ('body' in pushes[0].keys()):
				msg2 = pushes[0]['body']
			if(msg2 == 'Off'):
				entered = False
				msg2 = 'Off'
				print('Turning Lights Off')
				pb.push_note("Home Automation System","Light is Off!!")
				gpio.output(40, 1)
				
finally:
	gpio.cleanup()
