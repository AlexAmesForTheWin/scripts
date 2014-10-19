#Alex ames
#October 2014

import RPi.GPIO as GPIO, feedparser, time
 
DEBUG = 1
 
USERNAME = "#"     # just the part before the @ sign, add yours here
PASSWORD = "#"     
 
newMailOffSet = 1        # my unread messages never goes to zero, yours might
mailCheckFreq = 60      # check mail every 60 seconds
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18 # todo / May need to be changed
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
 
while True:
 
        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
 
        if DEBUG:
                print "Congradulations You have", newmails, "new emails!"
 
        if newmails > newMailOffSet:
                GPIO.output(GREEN_LED, True)
                GPIO.output(RED_LED, False)
        else:
                GPIO.output(GREEN_LED, False)
                GPIO.output(RED_LED, True)
 
        time.sleep(mailCheckFreq)
!
