#!/usr/bin/env python

import imutils
import cv2
import numpy as np
from ShapeDetector import ShapeDetector

from imutils import perspective
from imutils import contours
from DrawFrame import DrawFrame

#~ #KINECT CAMERA VALUES
fx = 554.255
fy = 554.255
cx = 640/2
cy = 480/2
camera_matrix = np.array(([fx,0.,cx],[0.,fy,cy],[0.,0.,1.]))
frame_length = 0.25

#Define Object Points
owidth = 0.7
oheight = 0.5
object_points = np.array(([(0,oheight,0)],[(0,0,0)],[(owidth,0,0)]
	,[(owidth,oheight,0)]),dtype=float)
	
#Performs segmentisation of the background
cv_image = cv2.imread("Images/Plate(10mm).png")
gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY_INV)[1]

#Find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#Performs segmentisation of the background
gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY_INV)[1]

#find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for c in cnts:
	
	# Approximate Contours
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.04 * peri, True)

	# draw the contour (red)
	cv2.drawContours(cv_image, [approx], -1, (0, 0, 255), 2)
				
	# draw contour points (green)
	n1 = approx.shape
	for x in range(int(n1[0])):
		cv2.circle(cv_image, (int(approx[x,0,0]), int(approx[x,0,1])), 
			4, (0, 255, 0), -1)
	
	#Load image points into the image_points array
	image_points = np.zeros((4,1,2), dtype=float)
	for x in range(4):
		image_points[x][0][0] = approx[x][0][0]
		image_points[x][0][1] = approx[x][0][1]
		
	#The translation units are returned in the same units used for the object_points.
	retval, orvec, otvec = cv2.solvePnP(object_points, image_points, 
		camera_matrix, None, None, None, False, cv2.ITERATIVE)
	
	print "Output Translational Vector:"
	print otvec
	
	orm = np.zeros((3,3))
	ojm = np.zeros((3,9))
	cv2.Rodrigues(orvec, orm, ojm)
	
	print "Output Rotational Matrix:"
	print orm
			
df = DrawFrame()
df.draw_coord_frame(cv_image, camera_matrix, 
	otvec, orvec, frame_length)
			
cv2.imshow("Image window", cv_image)
cv2.waitKey(0)
	



