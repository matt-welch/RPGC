#!/usr/bin/env python
# Simulator.py
# run this program at the commabd line with the command: "python ./Simulator.py"
#
# dependencies: should have pip installed, RPi.GPIO
#
#
# Written by Matt Welch for Raspberry Pi Garden Controller project

import os
import sys
import time
import random

gsimHrsPerSec = 1
LEDSTATUS=True
LEDS = []
PROGMODE = "sim" #  or "real" when using GPIO

class Event: 
    """ Event class to hold generic events on GPIO pins """
    def __init__(self, pin, time, setting):
        self.pin = pin # a GPIO pin
        self.time = time # a time in decimal
        assertError = "{0} is not a valid setting for a GPIOPIN".format(setting)
        assert ((setting == "on") or (setting == "off")), assertError
        self.setting = setting # a string representing the pin action

    def action():
        self.pin.setStatus(setting)

eventList = [Event(11,7.0,"on"), Event(12, 8.0, "on"), Event(11,9.0, "off"), Event(12,10.0,"on")]

if(PROGMODE == "real"):
    import RPi.GPIO as GPIO
    validGPIOPins=[       7,    11,     12,    13,      15,     16,     18     ,22]
    validGPIONames=["GPIO7","GPIO0","GPIO1","GPIO2","GPIO3","GPIO4","GPIO5","GPIO6"]

    class GPIOPIN:
        """class to contain operations and settings for a GPIO pin"""
        boardSetup = False
        validPins=[7,11,12,13,15,16,18,22]
        pinsInUse=[]
        minPin = 10 # verify that this is (min(PIN numbers)
        maxPin = 20 # verify that this is (max(PIN numbers)
    
        def setup(self):
            # setup common to all GPIO devices (static method, only need to call once)
            if (boardSetup == False):
                GPIO.setmode(GPIO.BOARD)
                boardSetup = True
            
        def __init__(self, pinParam, mode="out"):
            assertError = "{0} is not a valid GPIO pin: select integers {1} to {2}".format(pinParam, self.minPin, self.maxPin)
            assert (pinParam <= maxPin and pinParam >= minPin), assertError
            self.setup(self)
            self.pin = pinParam
            if (mode == "out"):
                self.mode = GPIO.OUT
            else: 
                self.mode = GPIO.IN
            GPIO.setup(self.pin, self.mode)
    
        def on(self):
            self.status = "on"
            GPIO.output(self.pin, GPIO.HIGH)
            return
    
        def off(self):
            self.status = "off"
            GPIO.output(self.pin, GPIO.LOW)
            return
        
        def setLevel(self, level):
            # set the GPIO to an arbitrary value (TODO 0-3.3 v?)
            self.status = string(level)
            # TODO: verify the level is in range
            print( "Pin {0} set to {1:0.00}v".format(self.pin, self.status) )
            # TODO set pin level here
            return
    
        def setStatus(self, status):
            if (status=="on"):
                self.on()
            elif (status == "off" ):
                self.off()
            elif (type(status) == type(float)):
                self.setLevel(self, status)
            return
    
        def strobe(self, sleepTime):
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            return


class Light:
    """class to simulate the operation of a light"""
    def toggle(self):
       self._status = not(self._status)

    def setStatus(newstatus=False):
        self._status = newstatus

    def __init__(self, ident=0, gpiopin=0, status=False):
        self._status = status
        self._id = ident
        self.gpiopin = gpiopin
        self._counter = 0 # always initially 0
        

def toggleLED():
    global LEDSTATUS
    LEDSTATUS = not(LEDSTATUS)
    if LEDSTATUS:
        output = "on"
    else:
        output = "off"
    return output

def showAllStatus():
    line1 = ""
    for led in LEDS:
        line1 += "=LED({0:2d})=".format(led.gpiopin)
    print( line1 )
    line2 = ""
    for led in LEDS:
       line2 += "  {0}  ".format(led._status)
    print( line2 )
        
def switchRadomLED():
    L = random.randint(0,len(LEDS)-1)
    LEDS[L].toggle()
    

def main():
    print "Welcome to the Raspberri Pi Garden Controller Simulator"
    # define a list of lights
    random.seed(None)
    pinoffset = 0 # integer representing the lowest numbered GPIO pin - 1
    validPins=[7,11,12,13,15,16,18,22]
    for e in eventList: print("GPIOPin: {0}, trigger time: {1}, setting: {2}")
    pincount=0
    for pin in validPins:
        if (PROGMODE == "sim"):
            LEDS.append(Light(pincount, pin, False))
            pincount += 1
        elif (PROGMODE == "real"):
            LEDS.append(Light(pincount, pin , False))
            pincount += 1
        else:
            print("Invalid mode '{0}' specified")
            sys.exit()
            

    while(1):
        for i in range(0,24):
            print( "It's {0}:00: ".format(i) )
            print( "LED status = {0}".format(toggleLED()) )
            showAllStatus()
            switchRadomLED()
            time.sleep(gsimHrsPerSec)
    
    if (PROGMODE == "real"):
        GPIO.cleanup()



if __name__ == "__main__":
    main()
