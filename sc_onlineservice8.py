import wiringpi as wpi
import urllib2
import time
import os

wpi.wiringPiSetup()
wpi.pinMode(2,1)
command = "sudo ifconfig wlan0 up"
command2 = "sudo /etc/init.d/networking restart"

while True:
	try:
	    urllib2.urlopen("http://216.58.192.142")
	    wpi.digitalWrite(2,1)
	    time.sleep(1)
	    """ print "conection ok"""
	    wpi.digitalWrite(2,0)
	    time.sleep(1)
	except urllib2.URLError as err:
	    """print "no connection"""
            wpi.digitalWrite(2,0)
	    time.sleep(1)
	    os.system(command)
	    time.sleep(1)
	    os.system(command2)
