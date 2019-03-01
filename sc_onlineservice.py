import wiringpi as wpi
import urllib2
import time

wpi.wiringPiSetup()
wpi.pinMode(2,1)

while True:
	try:
	    wpi.digitalWrite(2,1)
	    """ print "conection ok"""
	    time.sleep(1)
	    wpi.digitalWrite(2,0)
	    time.sleep(1)
	except urllib2.URLError as err:
	    """print "no connection"""
            wpi.digitalWrite(2,1)
