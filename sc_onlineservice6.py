import wiringpi as wpi
import urllib2
import time

wpi.wiringPiSetup()
wpi.pinMode(2,1)

while True:
	try:
	    urllib2.urlopen("http://216.58.192.142", timeout=1)
	    wpi.digitalWrite(2,1)
	    """ print "conection ok"""
	except urllib2.URLError as err:
	    """print "no connection"""
            wpi.digitalWrite(2,0)
