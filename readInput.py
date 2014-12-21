from time import sleep
import RPi.GPIO as GPIO
lights = [7,15,16,18,22]
inputPins = [13]
OFF = GPIO.LOW
ON = GPIO.HIGH

def setLights():
    GPIO.setmode(GPIO.BOARD)
    for light in lights:
        GPIO.setup(light, GPIO.OUT)
	
     
def turnOffOnePin(light):
   GPIO.output(light, GPIO.LOW)

def turnOnOnePin(light):
   GPIO.output(light, GPIO.HIGH)

def setupInput():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inputPins[0], GPIO.IN)


def turnOffPins():
    for light in lights: 
        print("Turning off GPIO {0}".format(light))
        GPIO.output(light, GPIO.LOW)
        sleep(0.5)

def turnOnPins():
    for light in lights: 
        print("Turning on GPIO {0}".format(light))
        GPIO.output(light, GPIO.HIGH)
        sleep(0.5)

def main():
    setLights()
    turnOffPins()
    turnOnPins()
    turnOffPins()
    
    setupInput()
    while 1:
        input = GPIO.input(inputPins[0])
        print type(input), input
	print("The current voltage is {0}".format(input))
        sleep(0.5)

    while 1:
         for light in lights:
              print("Turning on LED({0})".format(light)) 
              turnOnOnePin(light)              

              sleep(1)

              print("Turning off LED({0})".format(light)) 
              turnOffOnePin(light)              
              sleep(1)

if __name__ == "__main__":
    main();
