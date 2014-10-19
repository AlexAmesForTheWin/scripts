# author Alex Ames, March 1st 2013
# Module credit goes to the Opencv/SimpleCV teams, Thank you! 

from SimpleCV import *


# This script binarizes your photos

img = Image('#')
imgBin = img.binarize(50)
imgBin.save('#')
imgBin.show()
