#!/usr/bin/env python
# Simulator.py
# run this program at the commabd line with the command: "python ./Simulator.py"
#
# Written by Matt Welch for Raspberry Pi Garden Controller project

import os
import sys
import time

gsimHrsPerSec = 1
LEDSTATUS=True

def toggleLED():
    global LEDSTATUS
    LEDSTATUS = not(LEDSTATUS)
    if LEDSTATUS:
        output = "on"
    else:
        output = "off"

    return output

def main():
    print "Welcome to the Raspberri Pi Garden Controller Simulator"
    

    while(1):
        for i in range(0,24):
            print "It's {0}:00: ".format(i)
            print "LED status = {0}".format(toggleLED())
            time.sleep(gsimHrsPerSec)
    


if __name__ == "__main__":
    main()
