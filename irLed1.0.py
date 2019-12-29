import RPi.GPIO as GPIO
import math
import os
from datetime import datetime
from time import sleep

# This is for revision 1 of the Raspberry Pi, Model B
# This pin is also referred to as GPIO23
INPUT_WIRE = 18
Key_0="0x100ff6897L"
Key_1="0x100ff30cfL"
Key_2="0x100ff18e7L"
Key_3="0x100ff7a85L"
Key_4="0x100ff10efL"
Key_5="0x100ff38c7L"
Key_6="0x100ff5aa5L"
Key_7="0x100ff42bdL"
Key_8="0x100ff4ab5L"
Key_9="0x100ff52adL"

LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 11
LED_G = 9
LED_DP = 10
#OUTPUT_GPIO= 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_WIRE, GPIO.IN)
#GPIO.setup(OUTPUT_GPIO,GPIO.OUT)

GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(LED_C, GPIO.OUT)
GPIO.setup(LED_D, GPIO.OUT)
GPIO.setup(LED_E, GPIO.OUT)
GPIO.setup(LED_F, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_DP,GPIO.OUT)

def showDigit(num, showDotPoint):
    if (num == 0) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not False)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not True)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 1) :
        GPIO.output(LED_A, not True)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not True)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not True)
        GPIO.output(LED_G, not True)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 2) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not True)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not False)
        GPIO.output(LED_F, not True)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 3) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not True)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 4) :
        GPIO.output(LED_A, not True)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not True)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 5) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not True)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 6) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not True)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not False)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 7) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not True)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not True)
        GPIO.output(LED_G, not True)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 8) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not False)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)
    elif (num == 9) :
        GPIO.output(LED_A, not False)
        GPIO.output(LED_B, not False)
        GPIO.output(LED_C, not False)
        GPIO.output(LED_D, not False)
        GPIO.output(LED_E, not True)
        GPIO.output(LED_F, not False)
        GPIO.output(LED_G, not False)
        GPIO.output(LED_DP, not showDotPoint)


while True:
	value = 1
	# Loop until we read a 0
	while value:
		value = GPIO.input(INPUT_WIRE)

	# Grab the start time of the command
	startTime = datetime.now()

	# Used to buffer the command pulses
	command = []

	# The end of the "command" happens when we read more than
	# a certain number of 1s (1 is off for my IR receiver)
	numOnes = 0

	# Used to keep track of transitions from 1 to 0
	previousVal = 0

	while True:

		if value != previousVal:
			# The value has changed, so calculate the length of this run
			now = datetime.now()
			pulseLength = now - startTime
			startTime = now

			command.append((previousVal, pulseLength.microseconds))

		if value:
			numOnes = numOnes + 1
		else:
			numOnes = 0

		# 10000 is arbitrary, adjust as necessary
		if numOnes > 10000:
			break

		previousVal = value
		value = GPIO.input(INPUT_WIRE)
	
        binaryString = "".join(map(lambda x: "1" if x[1] > 1000 else "0", filter(lambda x: x[0] == 1, command)))
#        print(binaryString)
        hexString=hex(int(binaryString,2))
#        print(hexString)
        if hexString==Key_0:
            showDigit(0,True)
        elif hexString==Key_1:
            showDigit(1,True)
	elif hexString==Key_2:
            showDigit(2,True)
	elif hexString==Key_3:
            showDigit(3,True)
	elif hexString==Key_4:
            showDigit(4,True)
	elif hexString==Key_5:
            showDigit(5,True)
	elif hexString==Key_6:
            showDigit(6,True)
	elif hexString==Key_7:
            showDigit(7,True)
	elif hexString==Key_8:
            showDigit(8,True)
	elif hexString==Key_9:
            showDigit(9,True)
