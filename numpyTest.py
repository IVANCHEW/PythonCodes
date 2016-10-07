import numpy as np


#Each list contains the 3D coordinates of an object
A = [0.,0.,0.]
B = [0.5,0.,0.]
C = [0.5,0.7,0.]
D = [0.,0.7,0.]
E = [0.,0.,0.01]
F = [0.5,0.,0.01]
G = [0.5,0.7,0.01]
H = [0.,0.7,0.01]

#The following code creates a Nx1 3 channel array out of the coordinates.
#~ Object_points = np.array((A,B,C,D,E,F,G,H), dtype = float)
Object_points = np.array(([A],[B],[C],[D],[E],[F],[G],[H]), dtype = float)

a = Object_points.shape

print a

no_of_points = 8

image_points = np.zeros((no_of_points,1,2))
image_points[0][0][0] = 3.
c = image_points.shape

print c
print image_points

camera_matrix = np.array(([3,0,0],[0,1,1],[0,0,1]))
d = camera_matrix.shape

print d

P=np.zeros((4,3))

e = P.shape
print P
print e

A = (0,0)
print A
