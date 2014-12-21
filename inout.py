from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.LOW)
sleep(1)
GPIO.output(13, GPIO.HIGH)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15,GPIO.LOW)
sleep(1)
GPIO.output(15, GPIO.HIGH)

GPIO.setup(7, GPIO.IN)
GPIO.setup(12, GPIO.IN)
while 1:
	if GPIO.input(12):
		GPIO.output(15, GPIO.LOW)
	else:
		GPIO.output(15, GPIO.HIGH)

	sleep(1)
	if GPIO.input(7):
		GPIO.output(13, GPIO.LOW)
	else:
		GPIO.output(13, GPIO.HIGH)
		
