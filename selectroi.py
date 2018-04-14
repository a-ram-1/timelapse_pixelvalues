#code modified from https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/

import cv2
import numpy as np
 
if __name__ == '__main__' :
	# Read image
	im = cv2.imread("pcj51_52/10.png")
	 
	# Select ROI
	fromCenter = False
	r = cv2.selectROI(im, fromCenter)
	 
	# Crop image
	#imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
	r0r2 = int(r[0])+int(r[2])
	r1r3 = int(r[1])+int(r[3])
	print "upper left: (" + str(r[0])+", "+ str(r[1]) + "), " + "bottom right: (" + str(r0r2)+ ", " + str(r1r3) + ")"
 
	# Display cropped image
	cv2.imshow("Image", im)
	cv2.waitKey(0)

