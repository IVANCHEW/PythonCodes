import math
import numpy as np

def dhmatrix(a, twist, offset, deg):
	dh = np.zeros((4,4))
	dh[0][0] = math.cos(deg);
	dh[0][1] = -1*math.sin(deg)*math.cos(twist)
	dh[0][2] = math.sin(deg)*math.sin(twist)
	dh[0][3] = offset*math.cos(deg)
	
	dh[1][0] = math.sin(deg)
	dh[1][1] = math.cos(deg)*math.cos(twist)
	dh[1][2] = -1*math.cos(deg)*math.sin(twist)
	dh[1][3] = offset*math.sin(deg)
	
	dh[2][1] = math.sin(twist)
	dh[2][2] = math.cos(twist)
	dh[2][3] = a
	
	dh[3][3] = 1
	
	return dh
	
def rpyTransform(r1,r2,r3):
	
	rpy = np.zeros((3,3))
	rpy[0][0] = math.cos(r1)*math.cos(r2)
	rpy[0][1] = -1*math.sin(r1)*math.cos(r3)+math.cos(r1)*math.sin(r2)*math.sin(r3)
	rpy[0][2] = math.sin(r1)*math.sin(r3) + math.cos(r1)*math.sin(r2)*math.cos(r3)
	
	rpy[1][0] = math.sin(r1)*math.cos(r2)
	rpy[1][1] = math.cos(r1)*math.cos(r3) + math.sin(r1)*math.sin(r2)*math.sin(r3)
	rpy[1][2] = -1*math.cos(r1)*math.sin(r3) + math.sin(r1)*math.sin(r2)*math.cos(r3)
	
	rpy[2][0] = -1*math.sin(r2)
	rpy[2][1] = math.cos(r2)*math.sin(r3)
	rpy[2][2] = math.cos(r2)*math.cos(r3)
	
	return rpy	
	
def eulerTransform(r1,r2,r3):
	
	euler = np.zeros((3,3))
	euler[0][0] = math.cos(r1)*math.cos(r2)*math.cos(r3) - math.sin(r1)*math.sin(r3)
	euler[0][1] = -1*(math.cos(r1)*math.cos(r2)*math.sin(r3)+math.sin(r1)*math.cos(r3))
	euler[0][2] = math.cos(r1)*math.sin(r2)
	
	euler[1][0] = math.sin(r1)*math.cos(r2)*math.cos(r3) + math.cos(r1)*math.sin(r3)
	euler[1][1] = -1*math.sin(r1)*math.cos(r2)*math.sin(r3) + math.cos(r1)*math.cos(r3)
	euler[1][2] = math.sin(r1)*math.sin(r2)
	
	euler[2][0] = -1*math.sin(r2)*math.cos(r3)
	euler[2][1] = math.sin(r2)*math.sin(r3)
	euler[2][2] = math.cos(r2)
	
	return euler

def getRPY(a):
	r11 = a[0][0]
	r12 = a[0][1]
	r13 = a[0][2]
	r21 = a[1][0]
	r22 = a[1][1]
	r23 = a[1][2]
	r31 = a[2][0]
	r32 = a[2][1]
	r33 = a[2][2]	
	
	roll = math.atan2(r21,r11)
	pitch = math.atan2(-r31,math.sqrt(math.pow(r32,2)+math.pow(r33,2)))
	yaw = math.atan2(r32,r33)
	print "deg1: %.2f, deg2: %.2f, deg3: %.2f" % (roll*180/PI, pitch*180/PI, yaw*180/PI)
	
def inverseK(x0, y0, z0, a20, a30, d10):
	x = float(x0)
	y = float(y0)
	z = float(z0)
	a2 = float(a20)
	a3 = float(a30)
	d1 = float(d10)
	r = math.sqrt(pow(x,2) + pow(y,2))
	s = z - d1
	
	if (r>(a2+a3)):
		print "Error, out of reach of configuration"
	else:
		R = math.sqrt(pow(r,2) + pow((z-d1),2))
		
		#DETERMINING DEG1
		if x==0 and y>0:
			deg1 = PI/2
		elif x==0 and y<0:
			deg1 = -PI/2
		elif x<0 and y==0:
			deg1 = -PI
		elif x>0 and y==0:
			deg1 = 0
		elif x<0 and y<0:
			deg1 = math.atan(y/x) + PI
		elif x==0 and y==0:
			deg1 = 0
		else:
			deg1 = math.atan(y/x)
			
			
		#DETERMINING DEG 2 AND DEG 3
		d = (pow(r,2)+pow((s),2)- pow(a2,2) - pow(a3,2))/(2*a2*a3)
		
		if d<=1 and d>0:
			deg3 = math.atan(-1*math.sqrt(1-pow(d,2))/d)
			
			if s>0 and r<>0:
				deg2 = math.atan((s)/r) + math.atan((a3*math.sin(-deg3))/
				(a2+a3*math.cos(-deg3)))
			elif r==0 and s>0:
				deg2 = PI/2
			else:
				deg2 = math.atan((a3*math.sin(-deg3))/
				(a2+a3*math.cos(-deg3)))
			
		elif d==0:
			deg3 = - PI/2
			
			deg2 = math.atan((s)/r) + math.atan((a3*math.sin(-deg3))/
			(a2+a3*math.cos(-deg3)))
			
		elif d>=-1 and d<0:
			deg3 = math.atan(-1*math.sqrt(1-pow(d,2))/d) - PI
			
			if s>0 and r<>0:
				deg2 = (math.atan((s)/r) - math.atan((a3*math.sin(deg3))/
				(a2+a3*math.cos(deg3))))
			else:
				deg2 = -(math.atan((s)/r) + math.atan((a3*math.sin(deg3))/
				(a2+a3*math.cos(deg3))))
		
		
		
		output = np.zeros((3))
		output[0] = deg1*180/PI
		output[1] = deg2*180/PI
		output[2] = deg3*180/PI
		print "d: %.2f, R: %.2f" % (d,R)
		return output


	
#START OF CODE
PI = math.pi

#~ link_length = np.zeros((5))
#~ link_twist = np.zeros((5))
#~ link_offset = np.zeros((5))
#~ link_deg = np.zeros((5))
#~ dh = np.zeros((5,4,4))
#~ point = np.zeros((4))

#~ n_links = 4

#~ #Fixed
#~ deg0 = 0
#~ #Revolute Joint 1
#~ deg1 = 0
#~ #Revolute Joint 2
#~ deg2 = 0
#~ #Revolute Joint 3
#~ deg3 = 0

#~ l1 = 10
#~ l2 = 10
#~ l3 = 10
#~ l4 = 10

#~ point[0] = 0
#~ point[1] = 0
#~ point[2] = 0
#~ point[3] = 1

#~ #Get inverse
#~ inverseAngles = inverseK(0,0,40,l3,l4,(l1+l2))
#~ print "Inverse Angles: deg1: %.2f, deg2: %.2f, deg3: %.2f" % (inverseAngles[0], inverseAngles[1], inverseAngles[2])

#~ #Input variables for Forward Kinematics
#~ deg1 = inverseAngles[0]
#~ deg2 = inverseAngles[1]
#~ deg3 = inverseAngles[2]

#~ #Input fixed values for Forward Kinematics
#~ link_length[0] = l1
#~ link_twist[0] = 0
#~ link_offset[0] = 0
#~ link_deg[0] = 0

#~ link_length[1] = l2
#~ link_twist[1] = PI/2
#~ link_offset[1] = 0
#~ link_deg[1] = deg1*PI/180

#~ link_length[2] = 0
#~ link_twist[2] = 0
#~ link_offset[2] = l3
#~ link_deg[2] = (deg2)*PI/180

#~ link_length[3] = 0
#~ link_twist[3] = 0
#~ link_offset[3] = l4
#~ link_deg[3] = deg3*PI/180

#link_length[4] = 0
#link_twist[4] = 0
#link_offset[4] = 0
#link_deg[4] = 0

#~ #Calculate Rotation Matrix
#~ for x in range(0,n_links):
	#~ dh[x] = dhmatrix(link_length[x],link_twist[x],link_offset[x],link_deg[x])
	#print "a %d" % x
	#print dh[x]

#~ #Calculate point w.r.t to world coordinate	
#~ result=np.dot(dh[n_links-1],point)

#~ for x in range(1,n_links):
	#~ result=np.dot(dh[n_links-1-x],result)

#print "Deg1: %.2f, Deg2: %.2f, Deg3: %.2f" % (deg1,deg2,deg3)
#~ print "Resulting point: x: %.2f, y: %.2f, z: %.2f" % (result[0], result[1], result[2])

rpy = rpyTransform(0,45*PI/180,(90-39.27)*PI/180)
print "rpy matrix:"
print rpy

euler = eulerTransform(2.178, -0.422, 1.029)
print "Euler matrix:"
print euler

## EULER MATRIX TEST
#~ deg1 = 2.178
#~ deg2 = -0.422
#~ deg3 = 1.029

#~ b = np.zeros((3,3,3))
#~ b[0][2][2] = 1
#~ b[0][0][0] = math.cos(deg1)
#~ b[0][0][1] = -math.sin(deg1)
#~ b[0][1][0] = math.sin(deg1)
#~ b[0][1][1] = math.cos(deg1)

#~ b[1][1][1] = 1
#~ b[1][0][0] = math.cos(deg2)
#~ b[1][0][2] = math.sin(deg2)
#~ b[1][2][0] = -math.sin(deg2)
#~ b[1][2][2] = math.cos(deg2)

#~ b[2][2][2] = 1
#~ b[2][0][0] = math.cos(deg3)
#~ b[2][0][1] = -math.sin(deg3)
#~ b[2][1][0] = math.sin(deg3)
#~ b[2][1][1] = math.cos(deg3)

#~ c1 = np.dot(b[1],b[2])
#~ c2 = np.dot(b[0],c1)

#~ print c2

a = np.zeros((3,3))
#~ a[0][0] = 0.63441225
#~ a[0][1] = -0.54158259
#~ a[0][2] = 0.55155181

#~ a[1][0] = -0.00217854
#~ a[1][1] = -0.00217854
#~ a[1][2] = -0.6993504

#~ a[2][0] = 0.77299182
#~ a[2][1] = 0.44247488 
#~ a[2][2] = -0.45464231

## 2nd

#~ a[0][0] = 0.63105324
#~ a[0][1] = -0.54229819
#~ a[0][2] = 0.55469315

#~ a[1][0] = -0.00683602 
#~ a[1][1] = -0.71891055 
#~ a[1][2] = -0.69506898

#~ a[2][0] = 0.77570941
#~ a[2][1] = 0.43483364
#~ a[2][2] = -0.45737799

## 3rd

#~ a[0][0] = 0.63441225
#~ a[0][1] = -0.54158259
#~ a[0][2] = 0.55155181

#~ a[1][0] = -0.00217854
#~ a[1][1] = -0.00217854
#~ a[1][2] = -0.6993504

#~ a[2][0] = 0.77299182
#~ a[2][1] = 0.44247488 
#~ a[2][2] = -0.45464231

## 4th

a[0][0] = 0.63324449
a[0][1] = -0.5455968
a[0][2] = 0.54893127

a[1][0] = -0.00560004
a[1][1] = -0.71246915 
a[1][2] = -0.70168109

a[2][0] = 0.77393155 
a[2][1] = 0.44126165
a[2][2] = -0.45422253

b = getRPY(a)

