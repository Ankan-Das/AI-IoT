import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)

try:
    while True:
          if GPIO.input(10) == GPIO.HIGH:
                GPIO.output(12,True)
                print("Button was Pushed")
                time.sleep(0.2)
          else:
                GPIO.output(12,False)
                time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
