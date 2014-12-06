#!/usr/bin/env python
# Simulator.py
# run this program at the commabd line with the command: "python ./Simulator.py"
#
# Written by Matt Welch for Raspberry Pi Garden Controller project

import os
import sys
import time
import random

gsimHrsPerSec = 1
LEDSTATUS=True
LEDS = []

class Light:
    """class to simulate the operation of a light"""
    def toggle(self):
       self._status = not(self._status)

    def setStatus(newstatus=False):
        self._status = newstatus

    def __init__(self, ident=0, status=False):
        self._status = status
        self._id = ident
        self._counter = 0 # always initialy 0
        

def toggleLED():
    global LEDSTATUS
    LEDSTATUS = not(LEDSTATUS)
    if LEDSTATUS:
        output = "on"
    else:
        output = "off"

    return output

def showiAllStatus():
    n = len(LEDS)
    line1 = ""
    for i in range(0,n):
        line1 += "=LED({0})=".format(i)
    print line1
    line2 = ""
    for led in LEDS:
       line2 += " {0}  ".format(led._status)
    print line2
        
def switchRadomLED():
    L = random.randint(0,len(LEDS)-1)
    LEDS[L].toggle()
    

def main():
    print "Welcome to the Raspberri Pi Garden Controller Simulator"
    # define a list of lights
    random.seed(None)
    for i in range(0,10):
        LEDS.append(Light(i,False))

    while(1):
        for i in range(0,24):
            print "It's {0}:00: ".format(i)
            print "LED status = {0}".format(toggleLED())
            showiAllStatus()
            switchRadomLED()

            time.sleep(gsimHrsPerSec)
    


if __name__ == "__main__":
    main()
