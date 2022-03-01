import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711
    



def scaleSetup():
    referenceUnit = 1
    hx = HX711(19, 13)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    hx.reset()
    hx.tare()
    print("Tare done! Add weight now...")
    return hx

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()
    
def getWeight(hx):
    val = 0
    for i in range(10):
        val += hx.get_weight(5)
        print(val)
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
    cleanAndExit()
    return val / 10



