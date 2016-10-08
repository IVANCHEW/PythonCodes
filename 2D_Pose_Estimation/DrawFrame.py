import numpy as np
import math
import cv2
#TASK: Not yet able to properly define size of frame
#TASK: Put the frame on the panel (DONE)
#CONTEXTUAL CODE

class DrawFrame:
	
	def __init__(self):
		pass
 
	def draw_coord_frame(self, cv_image, camera_matrix, tvec, rvec, frame_length):

		PI = math.pi

		#Coordinate Assignment
		P0 = np.zeros((3,3), dtype=float)
		P1 = np.zeros((3,3), dtype=float)

		#X
		P1[0][0] = frame_length
		#Y
		P1[1][1] = frame_length
		#Z
		P1[2][2] = frame_length

		#Assignment of frame center
		P=np.zeros((4,3), dtype=float)
		
		#~ P[0][0] = 0.35
		#~ P[0][1] = 0.25
		#~ P[0][2] = 0
		
		P[0][0] = 0
		P[0][1] = 0
		P[0][2] = 0

		#~ print P

		#Assignment of extension

		P[1][0] = P[0][0] + P1[0][0]
		P[1][1] = P[0][1] + P1[0][1]
		P[1][2] = P[0][2] + P1[0][2]

		P[2][0] = P[0][0] + P1[1][0]
		P[2][1] = P[0][1] + P1[1][1]
		P[2][2] = P[0][2] + P1[1][2]

		P[3][0] = P[0][0] + P1[2][0]
		P[3][1] = P[0][1] + P1[2][1]
		P[3][2] = P[0][2] + P1[2][2]

		#~ print "Points after transformation:"
		#~ print P

		#Plotting points
		image_points = cv2.projectPoints(P, rvec, tvec, camera_matrix, None)

		A = (int(image_points[0][0][0][0]),int(image_points[0][0][0][1]))
		B = (int(image_points[0][1][0][0]),int(image_points[0][1][0][1]))
		C = (int(image_points[0][2][0][0]),int(image_points[0][2][0][1]))
		D = (int(image_points[0][3][0][0]),int(image_points[0][3][0][1]))
		#B:x-axis, C:y-axis, D:z-axis

		#Red
		cv2.line(cv_image, A, B,(255,0,0), 2)
		#Green
		cv2.line(cv_image, A, C,(0,255,0), 2)
		#Yellow
		cv2.line(cv_image, A, D,(0,255,255), 2)

		return cv_image
