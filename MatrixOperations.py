def print_Matrix(Matrix):
	
	#Check suitability for printing
	#First condition checks if Matrix is multi-dimensional
	if isinstance(Matrix[0], list)==True:
		suitable = True
		Height = len(Matrix)
		
		#Ensures that every column has an equal number of rows
		Width = len(Matrix[0])
		for n in range(Width):
			if len(Matrix[n])<> Height:
				suitable = False
				break
					
		if suitable == True:
			print "Width: %d, Height %d" %(Width, Height)	
		
			#Printing the Matrix
			s = ""

			for y in range(Height):
				s= ""
				for x in range(Width):
					s = s + "%.1f " % Matrix[y][x]
				print s
		else:
			print "List not a matrix"
	else:
		Height = len(Matrix)
		for y in range(Height):
			print "%.1f" % Matrix[y]
			
def print_Matrix_Detailed(Matrix):
	
	#Check suitability for printing
	#First condition checks if Matrix is multi-dimensional
	if isinstance(Matrix[0], list)==True:
		suitable = True
		Height = len(Matrix)
		
		#Ensures that every column has an equal number of rows
		Width = len(Matrix[0])
		for n in range(Width):
			if len(Matrix[n])<> Height:
				suitable = False
				break
					
		if suitable == True:
			print "Width: %d, Height %d" %(Width, Height)	
		
			#Printing the Matrix
			s = ""

			for y in range(Height):
				s= ""
				for x in range(Width):
					s = s + "%.6f " % Matrix[y][x]
				print s
		else:
			print "List not a matrix"
	else:
		Height = len(Matrix)
		for y in range(Height):
			print "%.6f" % Matrix[y]

def multiply_Matrix(Matrix1, Matrix2):
	#Function to perform a cross multiplication of Matrix 1 with 2
	
	#Get sizes of matrixes
	HeightA = len(Matrix1)
	if isinstance(Matrix1[0], list)==True:
		WidthA = len(Matrix1[0])
	else:
		WidthtA=1
	HeightB = len(Matrix2)
	if isinstance(Matrix2[0], list)==True:
		WidthB = len(Matrix2[0])
	else:
		WidthB=1
	
	#Prepare the result matrix
	Matrix3 = []
	
	if WidthB==1:
		for n2 in range(HeightA):
			Matrix3.append(0)
	else:
		for n in range(WidthB):
			Matrix3.append([])
			
			for n2 in range(HeightA):
				Matrix3[n].append(0)
	
	#Check for suitability
	suitable = True
	
	if WidthA <> HeightB:
		suitable = False
		
	if suitable == True:
		#print "Suitable for multiplcation"
		
		#For multi-dimensionl arrays
		if WidthB > 1 and HeightA >1:
			for y in range(HeightA):
				for x in range(WidthB):				
					for x2 in range(WidthA):
						Matrix3[x][y] = Matrix3[x][y] + Matrix1[x2][y]*Matrix2[x][x2]
			
			return Matrix3
		
		#Results in a 1Row Matrix
		elif HeightA==1:
			for y in range(HeightA):
				for x in range(WidthB):				
					for x2 in range(WidthA):
						Matrix3[x][y] = Matrix3[x][y] + Matrix1[x2][y]*Matrix2[x][x2]
			
			return Matrix3
			
		#Results in a 1Column Matrix
		elif WidthB==1:
			for x in range(HeightB):				
				for x2 in range(WidthA):
					Matrix3[x] = Matrix3[x] + Matrix1[x][x2]*Matrix2[x2]
			
			return Matrix3
			
	else:
		print "Matrixes are not suitable for multiplication"

def get_Determinant_Matrix(Matrix):
	#From this point, matrix is assumed to be a square matrix
	n = len(Matrix)
	odd = 1

def get_Inverse_Matrix(Matrix):
	Width = len(Matrix)
	Height = len(Matrix[0])
	
	#Accept only square matrix
	
	#Prepare the result matrix
	Inverse = []
	
	#Creates the identify matrix of size nxn
	for n1 in range (Width):
		Inverse.append([])
		for n2 in range (Width):
			if n1==n2:
				Inverse[n1].append(1)
			else:
				Inverse[n1].append(0)
		
	#Begin calculation of inverse
	for n1 in range(Width):
		
		d = Matrix[n1][n1]
		
		#Division of Row N1 by the M[n][n]
		for n2 in range(Width):
			
			#?? When I ammend the value of Matrix like this, do I change a local matrix or the actual matrix used as the arguement?
			Matrix[n1][n2] = Matrix[n1][n2]/d
			Inverse[n1][n2] = Inverse[n1][n2]/d
			
		#Subtract of other Rows by Row N1
		if n1 <> Width-1:
			
			#loop through all rows below current row
			for n2 in xrange(n1+1,(Width),1):
				
				d= Matrix[n2][n1] / Matrix[n1][n1]
				
				for n3 in range(Width):
					
					Matrix[n2][n3]=Matrix[n2][n3]-d*Matrix[n1][n3]
					Inverse[n2][n3]=Inverse[n2][n3]-d*Inverse[n1][n3]

	#Refers order of subtraction: From bottom to top
	for n1 in range(Width-1):
		ref1=Width-n1-1
		
		#loop through all rows below current row
		for n2 in xrange(n1+1,(Width),1):
			
			ref2=Width-n2-1
			d= Matrix[ref2][ref1] / Matrix[ref1][ref1]
				
			for n3 in range(Width):
					
				Matrix[ref2][n3]=Matrix[ref2][n3]-d*Matrix[ref1][n3]
				Inverse[ref2][n3]=Inverse[ref2][n3]-d*Inverse[ref1][n3]
				
	
	return Inverse

def get_Trajectory_Coefficients(t0,x0,v0,a0,tf,xf,vf,af):
	
	#Trijactory Matrixes
	Trijac1 = [[],[],[],[],[],[]]
	Trijac2 = []
			
	Trijac2.append(x0)
	Trijac2.append(v0)
	Trijac2.append(a0)
	Trijac2.append(xf)
	Trijac2.append(vf)
	Trijac2.append(af)

	Trijac1[0].append(1)
	Trijac1[0].append(t0)
	Trijac1[0].append(t0**2)
	Trijac1[0].append(t0**3)
	Trijac1[0].append(t0**4)
	Trijac1[0].append(t0**5)

	Trijac1[1].append(0)
	Trijac1[1].append(1)
	Trijac1[1].append(2*t0)
	Trijac1[1].append(3*t0**2)
	Trijac1[1].append(4*t0**3)
	Trijac1[1].append(5*t0**4)

	Trijac1[2].append(0)
	Trijac1[2].append(0)
	Trijac1[2].append(2)
	Trijac1[2].append(6*t0)
	Trijac1[2].append(12*t0**2)
	Trijac1[2].append(20*t0**3)

	Trijac1[3].append(1)
	Trijac1[3].append(tf)
	Trijac1[3].append(tf**2)
	Trijac1[3].append(tf**3)
	Trijac1[3].append(tf**4)
	Trijac1[3].append(tf**5)

	Trijac1[4].append(0)
	Trijac1[4].append(1)
	Trijac1[4].append(2*tf)
	Trijac1[4].append(3*tf**2)
	Trijac1[4].append(4*tf**3)
	Trijac1[4].append(5*tf**4)

	Trijac1[5].append(0)
	Trijac1[5].append(0)
	Trijac1[5].append(2)
	Trijac1[5].append(6*tf)
	Trijac1[5].append(12*tf**2)
	Trijac1[5].append(20*tf**3)

	ITrijac1=get_Inverse_Matrix(Trijac1)
	Coeff = multiply_Matrix(ITrijac1, Trijac2)

	print "Coefficients from a0 to a5"
	print_Matrix_Detailed(Coeff)

#Only required to ammend these boundary conditions
t0=0.0
x0=0.0
v0=0.0
a0=0.0

tf=5.0
xf=1.57
vf=0.0
af=0.0

get_Trajectory_Coefficients(t0,x0,v0,a0,tf,xf,vf,af)
