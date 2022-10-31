#Python code for blinking LED for Raspberry pi
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,1)
time.sleep(1)
GPIO.output(11,0)
time.sleep(1)
GPIO.output(11,1)
time.sleep(1)
GPIO.output(11,0)
time.sleep(1)
GPIO.output(11,1)
time.sleep(1)
GPIO.cleanup()
