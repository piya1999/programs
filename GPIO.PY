from RPI import GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
sum=int(input("Sum :"))
d=a+b
if d==sum:
 GPIO.output(33,GPIO.HIGH)
 sleep(5)
else:
 GPIO.output(35,GPIO.HIGH)
 sleep(10)
