import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)

p = GPIO.PWM(19,100)     #PWM(<channel>,<Frequency>)

p.start(0)
try:
    while 1:
        for x in range(50):
              p.ChangeDutyCycle(x)
              time.sleep(0.1)
              
        time.sleep(1)
        
        for x in range(50)
              p.ChangeDutyCycle(50-x)
              time.sleep(0.1)
except: KeyboardInterrupt
GPIO.cleanup()
