#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)



while True:
    
    
    GPIO.output(4, True)
    time.sleep(5)
    GPIO.output(5, True)
    time.sleep(2)
    GPIO.output(4, False)
    GPIO.output(5, False)
    GPIO.output(6, True)
    time.sleep(5)
    GPIO.output(6, False)
    GPIO.output(5, True)
    time.sleep(2)
    GPIO.output(5, False)
    

