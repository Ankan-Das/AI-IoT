import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

TRIG = 12 
ECHO = 22
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

print ("Calibratng.....")
time.sleep(2)
print ("Place the object......")

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance+1.15, 2)
 
try:
    while True:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)

       while GPIO.input(ECHO)==0:
           pulse_start = time.time()

       while GPIO.input(ECHO)==1:
           pulse_end = time.time()
           
       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150
       distance = round(distance+1.15, 2)
	
       GPIO.output(32,0)
       GPIO.output(31,0)
       GPIO.output(33,0)
       GPIO.output(35,0)
     
       if  distance<10:
           GPIO.output(32,1)
           GPIO.output(31,1)
           GPIO.output(33,1)
           GPIO.output(35,1)
           time.sleep(0.5)
           print ("object too close")
           i=1

       if  distance<=15 and distance>=10:
           GPIO.output(32,1)
           GPIO.output(31,1)
           GPIO.output(33,1)
           GPIO.output(35,0)
           time.sleep(0.5)
           print ("distance:",distance,"cm")
           i=1
      
       if  distance<=20 and distance>15:
           GPIO.output(32,1)
           GPIO.output(31,1)
           GPIO.output(33,0)
           GPIO.output(35,0)
           time.sleep(0.5)
           print ("distance:",distance,"cm")
           i=1

       if  distance<=25 and distance>20:
           GPIO.output(32,1)
           GPIO.output(31,0)
           GPIO.output(33,0)
           GPIO.output(35,0)
           time.sleep(0.5)
           print ("distance:",distance,"cm")
           i=1

       if distance>25 and i==1:
           GPIO.output(32,0)
           GPIO.output(31,0)
           GPIO.output(33,0)
           GPIO.output(35,0)
           time.sleep(0.5)   
           print ("place the object....")
           i=0

except KeyboardInterrupt:
     GPIO.cleanup()
