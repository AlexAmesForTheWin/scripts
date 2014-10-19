# Alex Ames, credits go out to simpleCV/OpenCV teams for the great modules
# March 2013

from SimpleCV import *

img = Image("#")
binimg = img.binarize(150)
blobs = binimg.findBlobs()

blobs.show(width=10)



print "centers:", blobs.coordinates()

disp = Display((900,760))
while disp.isNotDone():
	if disp.mouseLeft:
		break 
	binimg.save(disp)
