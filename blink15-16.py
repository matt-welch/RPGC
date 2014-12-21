from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
while 1:
     print("Blinking {0}".format(15) )
     GPIO.output(15, False)
     sleep(1)
     GPIO.output(15, True)
     sleep(1)

     print("Blinking {0}".format(16) )
     GPIO.output(16, False)
     sleep(1)
     GPIO.output(16, True)
     sleep(1)

	 
