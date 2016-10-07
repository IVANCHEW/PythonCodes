#Function to check if list is homogeneous
def homogeneous_type(seq):
	iseq = iter(seq)
	first_type = type(next(iseq))
	return first_type if all((type(x) is first_type) for x in iseq) else False
		

value1 = 0

#List declaration
age = []
age.append(23.0)
age.append(1.0)

value1 = age[0]

#Retrieving value from a list for printing
print "Total age is %d" % (age[0])

#Using the funciton declared above
x=homogeneous_type(age)

#Determining the length of the array
list_Length = len(age)

if x==False:
	print "Array is not homogeneous"
#Unable to get this line to work
elif x=="<type 'int'>":
	print "Integer Array"
else:
	print "Array contains all elements of the same type"
	print x
	
print "Length of the list is %d" %(list_Length)

#Ammending the value of an array
age[0] = age[0]/2

#Display a float value
print "New age is %d" % (age[0])

#Determining a 1D Array
Matrix1D = []

Matrix1D.append(1)
Matrix1D.append(2)
Matrix1D.append(3)

len1 = len(Matrix1D)
con1 = isinstance(Matrix1D,list)
con2 = isinstance(Matrix1D[0],list)
print "Len 1 of Matrix: "

print len1
print con1
print con2
