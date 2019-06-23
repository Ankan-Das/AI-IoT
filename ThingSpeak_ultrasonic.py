import RPi.GPIO as GPIO
import urllib.request
import time
import math
#from bs4 import BeautifulSoup

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 12
ECHO = 22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)

print("Caliberating....")
time.sleep(2)
print("Place the Object....")

try:
	while True:
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		GPIO.output(TRIG,False)

		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration*17150
		distance = round(distance+1.15,2)
		
		data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=Q0P8D9GLKCHSMR7B&field2="+str(distance))
		print(data)
		time.sleep(3)
except KeyboardInterrupt:
	GPIO.cleanup()
