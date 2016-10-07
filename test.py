import numpy as np
import math
import cv2
from DrawFrame import DrawFrame
from ShapeDetector import ShapeDetector
import imutils
from imutils import perspective
from imutils import contours
PI = math.pi

#=====SET CAMERA PARAMETERS=====
cv_image = cv2.imread("images/panel5.png")
height, width= cv_image.shape[:2]

#Camera matrix determined from ROS camera_info topic
#Use rostopic echo /camera1/rgb/camera_info
#[PROBLEM] What is the fx and fy numbers?

fx = 554.255
fy = 554.255
cx = width/2
cy = height/2

print width
print height

#KINECT CAMERA VALUES
#[QUESTION] What are the units for the focal lengths given here?
#~ fx = 554.255
#~ fy = 554.255
#~ cx = 640/2
#~ cy = 480/2

camera_matrix = np.array(([fx,0.,cx],[0.,fy,cy],[0.,0.,1.]))

#TRANSLATION AND ROTATION MATRIX FOR CAMERA POSITION
rvec = np.zeros((3,3),dtype=float)
tvec = np.zeros((1,3),dtype=float)
for x in range(3):
	rvec[x][x]=1
	tvec[0][x]=0

tvec[0][0] = 0
tvec[0][1] = 0
tvec[0][2] = 0

#CONTEXTUAL INFORMATION
#rpy in deg (Clockwise direction)
rpy = np.zeros((3), dtype=float)
object_center = np.zeros((3), dtype=float)
#Roll
rpy[0] = 0
#Pitch
rpy[1] = -45
#Yaw
#~ rpy[2] = -50.73
rpy[2] = 50.73

#[PROBLEM] Pixel length doesn't translate to correct actual length
frame_length = 0.25

#=======BEGIN WORKING WITH IMAGE=======
#Determine Object Corner

#Performs segmentisation of the background
gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY_INV)[1]

#find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"]) 
	#~ cX = int((M["m10"] / M["m00"]) * ratio)
	#~ cY = int((M["m01"] / M["m00"]) * ratio)
	shape, approx = sd.detect(c)
	
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	#~ c = c.astype("float")
	#~ c *= ratio
	#~ c = c.astype("int")			
	
	display_text = "Contour: %d Approx: %d Test Value: %d" % (len(c),len(approx),camera_matrix[0][0])
	
	# draw the contour (red), center (blue), label (white), display (topleft, red)
	cv2.drawContours(cv_image, [approx], -1, (0, 0, 255), 2)
	cv2.circle(cv_image, (cX, cY), 5, (255, 0, 0), -1)
	cv2.putText(cv_image, shape, (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.putText(cv_image, display_text, (0, 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
	
	# draw contour points (green)
	n1 = approx.shape
	for x in range(int(n1[0])):
		cv2.circle(cv_image, (int(approx[x,0,0]), int(approx[x,0,1])), 
			4, (0, 255, 0), -1)

#=======BEGIN POSE DETERMINATION=========
#[PROBLEM] What are the units to be used for the object points definition? Pixel or meter units?
owidth = 0.7
oheight = 0.5
othick = 0.01
#Try defining a pure plane
#~ object_points = np.array(([(0,0,0)],[(owidth,0,0)],[(owidth,oheight,0)]
	#~ ,[(0,oheight,0)],[(0,0,othick)],[(owidth,0, othick)],[(owidth,oheight,othick)]
	#~ ,[(0,oheight,othick)]),dtype=float)
object_points = np.array(([(0,0,0)],[(owidth,0,0)],[(owidth,oheight,0)]
	,[(0,oheight,0)]),dtype=float)
	
image_points = np.zeros((4,1,2), dtype=float)
for x in range(4):
	image_points[x][0][0] = approx[x][0][0]
	image_points[x][0][1] = approx[x][0][1]

print "Image Points:"
print image_points

#The translation units are returned in the same units used for the object_points.
retval, orvec, otvec = cv2.solvePnP(object_points, image_points, 
	camera_matrix, None)

#object center in m
#Object center units should be the same as those used in the camera matrix
#xc
object_center[0] = otvec[0]
#yc
object_center[1] = otvec[1]
#zc
object_center[2] = otvec[2]

print "retval:"
print retval

print "Output Rotational Vector:"
print orvec

print "Output Translational Vector:"
print otvec

df = DrawFrame()
e_image = df.draw_coord_frame(cv_image, camera_matrix, otvec, orvec, frame_length)

cv2.imshow("Image window", cv_image)
cv2.imwrite("panelresult.png",cv_image)
cv2.waitKey(0)
