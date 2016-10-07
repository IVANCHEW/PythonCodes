def testfunction(n):
	n=n+1
	print "Function Variable:"
	print n

a=1

def testfunction2(n):
	n=n+3
	print "Function2 Variable:"
	print n
	return n

#This test will show if the function ammends the original variable

testfunction(a)

print "After Function:"
print a

#Demonstrates that the function does not ammend the variable. 
 
a = testfunction2(a)
print "After Function2:"
print a
#To ammend the local variable, a re-assignment is probably required
