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

		#rpy in deg (Clockwise direction)
		#~ Roll = rpy[0]
		#~ Pitch = rpy[1]
		#~ Yaw = rpy[2]

		#~ #object center in m
		#~ xc = object_center[0]
		#~ yc = object_center[1]
		#~ zc = object_center[2]

		#Coordinate Assignment
		P0 = np.zeros((3,3), dtype=float)
		P1 = np.zeros((3,3), dtype=float)
		#~ #X
		#~ P0[0][0] = 1.
		#~ #Y
		#~ P0[1][1] = 1.
		#~ #Z
		#~ P0[2][2] = 1.
		
		#X
		P1[0][0] = frame_length
		#Y
		P1[1][1] = frame_length
		#Z
		P1[2][2] = frame_length


		#Perform rotation
		#~ T = np.zeros((3,3,3), dtype = float)

		#~ r = -1*Roll/180. * PI
		#~ p = -1*Pitch/180. * PI
		#~ y = -1*Yaw/180. * PI

		#~ #Roll Transform
		#~ T[0][0][0] = math.cos(r)
		#~ T[0][0][1] = -math.sin(r)
		#~ T[0][1][0] = math.sin(r)
		#~ T[0][1][1] = math.cos(r)
		#~ T[0][2][2] = 1.

		#~ #Pitch Transform
		#~ T[1][1][1] = math.cos(p)
		#~ T[1][1][2] = -math.sin(p)
		#~ T[1][2][1] = math.sin(p)
		#~ T[1][2][2] = math.cos(p)
		#~ T[1][0][0] = 1

		#~ #Yaw Transform
		#~ #Pitch Transform
		#~ T[2][0][0] = math.cos(y)
		#~ T[2][0][2] = -math.sin(y)
		#~ T[2][2][0] = math.sin(y)
		#~ T[2][2][2] = math.cos(y)
		#~ T[2][1][1] = 1

		#~ print T

		#Rotation matrix determine by row x pitch x yaw (Rotation about current frame)
		#Rotation of rpy done according to the local frame
		#~ T0 = np.dot(T[0], T[1]) 
		#~ T1 = np.dot(T0, T[2])
		
		#~ #Rotation done according to the world frame
		#~ T0 = np.dot(T[2], T[1]) 
		#~ T1 = np.dot(T0, T[0])
		
		#~ print T0
		#~ print "Predefined Transformation Matrix:"
		#~ print T1

		#~ for x in range(3):
			#~ P1[x] = np.dot(T1 ,P0[x])

		#~ print P1

		#~ for x in range(3):
			#~ for x2 in range(3):
				#~ P1[x][x2] = P1[x][x2] * frame_length

		#~ print P1

		#Assignment of frame center
		P=np.zeros((4,3), dtype=float)
		#~ P[0][0] = xc
		#~ P[0][1] = yc
		#~ P[0][2] = zc
		P[0][0] = 0.35
		P[0][1] = 0.25
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

		print "Points after transformation:"
		print P

		#Plotting points
		image_points = cv2.projectPoints(P, rvec, tvec, camera_matrix, None)

		#~ print image_points[0]

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
