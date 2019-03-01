import wiringpi as wpi
import urllib2
import time

wpi.wiringPiSetup()
wpi.pinMode(2,1)

while True:
	wpi.digitalWrite(2,0)
        time.sleep(1)
	wpi.digitalWrite(2,1)
	time.sleep(1)
