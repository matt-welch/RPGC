'''
File: RPGClib.py
Author: Matthew Welch
Description: Library module containing wrapper API functions for the 
            generic RPi.GPIO library.  This library seeks to further
            constrain the GPIO functions to a more generic read/write
            paradigm.
'''



def Sensor:
    pass

def Switch:
    pass

def CondSwitch:
    pass

def TimedSwitch:
    pass

def OutputPIN(GPIOPIN):
    pass

class InputPin(GPIOPIN):
    """
    This is the generic class to represent a RaspberyPi GPIO pin
    configured as an input pin with associated reading and setting 
    methods
    """
    def __init__(self, arg):
        super(InputPin, self).__init__()
        self.arg = arg

class InputPin(GPIOPIN):
    """docstring for InputPin"""
    def __init__(self, pin):
        super(InputPin, self, pin).__init__()
    
class GPIOPIN( ):
    """class to contain operations and settings for a RaspberryPi GPIO pin"""
    boardInitialized=False # static
    validPins=[7,11,12,13,15,16,18,22] #should be const static
    validModes=[GPIO.LOW, GPIO.HIGH] # should be const static
    pinsInUse[] # should be static

    def setup(self):
        # setup common to all GPIO devices 
        # (static method, only need to call once)
        if (boardInitialized == False):
            boardInitialized = True
            GPIO.setmode(GPIO.BOARD)
        
    def __init__(self, paramPin, paramMode):
        super(GPIOPIN, self).__init__()
        self.setup(self)
        checkPin(self, paramPin)
        checkMode(self, paramMode)
        self.checkoutPin(self, pin)
        # should only change the mode if successful checkout
        self.setMode(self, paramMode)
    
    def checkMode(self, mode):
        """assert that the mode is a valid GPIO mode"""
        assertError = "{0} is not a valid GPIO MODE. Select GPIO.LOW or GPIO.HIGH".format(mode)
        assert (mode in validModes), assertError

    def checkPin(self, pin):
        """assert that the pin is in the validPins list"""
        assertError = "Error: PIN {0} is not valid ".format(pin)
        assert(pin in validPins) assertError

    def checkPinUse(self, pin):
        """assert that the pin is not in use"""
        assertError = "Error: pin {0} is in use".format(pin)
        assert(!(pin in pinsInUse)) assertError

    def checkoutPin(self, pin):
        """ remove pin from the pool of available pins """
        checkPin(self, pin)
        if( pin in pinsInUse ):
            checkPinUse(self,pin) 
        elif( pin in validPins ):
            self.pin = pin
            print "Pin {0} now checked out.  Issue checkinPin() to check it in".format(pin)
        else: 
            print("The pin specified ({0}) is not valid.  Please use only {1}".format(pin, validPins))

    def checkinPin(self, pin):
        """ return the pin to the list of pins that may be used """
        checkPin(self, pin)
        if( pin in pinsInUse ):
            pinsInUse.remove(pin)
            self.pin = 0
            setMode(self, GPIO.IN) # default state so don't accidentally emit charge
            print("Pin {0} is now reset.".format(pin))
        elif( pin in validPins ):
            print "Pin {0} was not in use.  It is available for use.".format(pin)
        else: 
            print("The pin specified ({0}) is not valid.  Please use only {1}".format(pin, validPins))
        
    def setMode(self, paramMode):
        """Sets the GPIO pin to GPIO.OUT or GPIO.IN"""
        checkMode(self, pin)
        self.mode = paramMode
        if (!(paramMode in [GPIO.OUT, GPIO.IN])):
            print "TODO: throw error here"
        GPIO.setup(self.pin, paramMode)




