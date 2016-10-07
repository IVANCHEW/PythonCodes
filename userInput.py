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
				deg2 = math.atan((s)/r) - math.atan((a3*math.sin(deg3))/
				(a2+a3*math.cos(deg3)))
			
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

s = raw_input('--> ')
PI = math.pi

if s == "close":
	print "Closing gripper"
elif s=="set":
	d = raw_input('Enter point value:')
	n=0
	deg =""
	out = []
	for letter in d:
		
		if letter == "," or letter =="":
			out.append(float(deg))
			#~ print out[n]
			n=n+1
			deg = ""
		else:
			deg = deg + letter
			
	#START OF CODE
	PI = math.pi

	link_length = np.zeros((5))
	link_twist = np.zeros((5))
	link_offset = np.zeros((5))
	link_deg = np.zeros((5))
	dh = np.zeros((5,4,4))
	point = np.zeros((4))

	n_links = 4

	#Fixed
	deg0 = 0

	l1 = 10
	l2 = 10
	l3 = 10
	l4 = 10

	point[0] = 0
	point[1] = 0
	point[2] = 0
	point[3] = 1

	#Get inverse
	inverseAngles = inverseK(out[0],out[1],out[2],l3,l4,(l1+l2))
	print "Inverse Angles: deg1: %.2f, deg2: %.2f, deg3: %.2f" % (inverseAngles[0], inverseAngles[1], inverseAngles[2])

	#Input variables for Forward Kinematics
	deg1 = inverseAngles[0]
	deg2 = inverseAngles[1]
	deg3 = inverseAngles[2]

	#Input fixed values for Forward Kinematics
	link_length[0] = l1
	link_twist[0] = 0
	link_offset[0] = 0
	link_deg[0] = 0

	link_length[1] = l2
	link_twist[1] = PI/2
	link_offset[1] = 0
	link_deg[1] = deg1*PI/180

	link_length[2] = 0
	link_twist[2] = 0
	link_offset[2] = l3
	link_deg[2] = (deg2)*PI/180

	link_length[3] = 0
	link_twist[3] = 0
	link_offset[3] = l4
	link_deg[3] = deg3*PI/180

	#~ link_length[4] = 0
	#~ link_twist[4] = 0
	#~ link_offset[4] = 0
	#~ link_deg[4] = 0

	#Calculate Rotation Matrix
	for x in range(0,n_links):
		dh[x] = dhmatrix(link_length[x],link_twist[x],link_offset[x],link_deg[x])
		#~ print "a %d" % x
		#~ print dh[x]

	#Calculate point w.r.t to world coordinate	
	result=np.dot(dh[n_links-1],point)

	for x in range(1,n_links):
		result=np.dot(dh[n_links-1-x],result)

	#~ print "Deg1: %.2f, Deg2: %.2f, Deg3: %.2f" % (deg1,deg2,deg3)
	print "Resulting point: x: %.2f, y: %.2f, z: %.2f" % (result[0], result[1], result[2])

elif s=="c":
	
	x=11.3
	y=0
	z=0
	
	#CONSTANTS
	a2 = 67.5
	a3 = 45
	d1 = 41.5
	
	r = math.sqrt(pow(x,2) + pow(y,2))
	print "r"
	print r
	
	deg1 = math.atan(y/x)
	print "deg1"
	print deg1
	
	
	
	d = (pow(r,2)+pow((z-d1),2)- pow(a2,2) - pow(a3,2))/(2*a2*a3)
	print "D"
	print d
	
	deg3a = math.atan(math.sqrt(1-pow(d,2))/d)
	
	print "deg3a"
	print deg3a*180/PI
	
	#~ deg3b = math.atan(math.sqrt(1-pow(d,2))/d)
	
	#~ print "deg3b"
	#~ print deg3b
	
	
	deg2 = math.atan((z-d1)/r) - math.atan((a3*math.sin(deg3a))/
		(a2+a3*math.cos(deg3a)))
	
	print "deg2"
	print deg2*180/PI

