#calculates mean pixel value for a given rectangular region

#import everything
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
#img = cv2.imread("image2.png") #you can uncomment the argparse part but this helps me remember what image I'm using

boundsfile = open("pcj_bounds_blue.txt", "a")
boundsfile.write(" \n")

#use click.py [also in this directory] to determine a rectangular region of interest
#specify this rectangle as 'img[lower right y:upper left y, upper left x:lower right x]'

upperleft = (484, 63)
lowerright = (514, 106)
cv2.rectangle(img,upperleft,lowerright,(0,255,0),1)

rect = img[upperleft[1]:lowerright[1], upperleft[0]:lowerright[0]]
mean = [rect[:, :, i].mean() for i in range(rect.shape[-1])]
mean = np.uint8([[mean]])
mean = cv2.cvtColor(mean, cv2.COLOR_BGR2HSV) #--might need to choose a color space that's not HSV
print "The mean HSV pixel value for the highlighted [in green] region is: " + str(mean)[2:-2] + ". Remember that OpenCV's HSV bounds are [179 255 255] whereas conventionally HSV goes by [360 100 100]." 

while True: 
	cv2.imshow('image',img)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("c"): 
		break
	
	if key == ord("p"): 
		boundsfile.write("\n The cell mean pixel value is " + str(mean)[2:-2])

	if key == ord("b"): 
		boundsfile.write("\n The background mean pixel value is " + str(mean)[2:-2])

cv2.destroyAllWindows()
