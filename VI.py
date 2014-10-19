# Author Alex Ames, March 3rd 2013, Visual Inspection
# modules Credit goes out to the SimpleCV/OpenCV teams, Thank you!!
# the '#' character needs to be changed to your local pictures
 



from SimpleCV import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Image source
img = Image("#")
img.save("#")
print("#")


#var's for usr input 
yes=0
no=1


#binarize photo option
usr_input = input("Would you Like to binarize Your Photo Source? \nPlease Write yes or no:  ") 
if usr_input == 0:
	 print("You have choosen to binarize your source:")
	 imgBin=img.binarize(150) # input a 0 to 255 value for binarization here.
         img=imgBin   
         imgBin.save("#")
else:
	print("your photo has not been processed:")
        img = Image("#") #rewrites img to orig source


print("") # just for space between lines


# binarized template processing:
usr_input2 = input("Write 'yes' to Template Match a Binzarized Image, \nWrite 'no'  to Template Match the Original Image: ")
if usr_input2 == 0:
    img_rgb = cv2.imread('#')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('#',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = .99     
    loc = np.where( res >= threshold)
    #print str(loc)
    trig_var = 1
    for pt in zip(*loc[::-1]):
       cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
       cv2.imwrite('resbin.png',img_rgb)
       img = Image("#")
else:
    trig_var = 2 

while True:
     if trig_var == 1:
		 #print("Your princess is in another castle")
		 break
     elif trig_var == 2:
         img_rgb = cv2.imread('#')
         img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
         template = cv2.imread('#',0)
         w, h = template.shape[::-1]
         res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
         threshold = .99   
         loc = np.where( res >= threshold)
         #print str(loc)
         for pt in zip(*loc[::-1]):
             cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
             cv2.imwrite('resbin.png',img_rgb)
             img = Image("#")
         break
print(" ")

#Feature detection options 
usr_input3 = input("Write a 'yes' or 'no' to initiate Feature Detection: ")
if usr_input3 ==0:
	 feats = img.findKeypoints()
         feats.draw(color=Color.BLUE)
         num_features = len (feats)
         print ("I Found This Many Features: " + str(num_features))
         trig_var2 = 2
         disp = Display((600,600))
else:
	trig_var2 = 3

while trig_var2 ==2:
	if num_features < 2000:
         print("Your stuff is Good.")
         break
	elif num_features > 2000:
         print("your stuff is bad.")
         break
	else:
	     print("You have choosen to not Detect Features")
             break
print("") 

print("A display window is being created please wait.")


#display settings!
disp = Display((600,600))
while disp.isNotDone():
	if disp.mouseLeft:
		break 
	img.save(disp)	
  
