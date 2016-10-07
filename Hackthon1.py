
def  numberOfPairs(a, k):
    
    b = []
    b = a
    t = len(b)
    y = 0
    
    for g in range(len(b)):
		
		print "%d, number: %d" % (g, b[g])
		
    while (y < t - 1):
		
		t2 = t - y
		found = False
		
		for y2 in range (t2-1):
			
			if b[y]==b[y+y2+1]:
				del b[y+y2+1]
				found = True
				break
				
		t = len(b)
		if found == False:
			y = y+1
				
	
    
    #n refers to the total number of elements
    n=len(b)
    Match = []
    count = 0
    
    for x in range(n-1):
        
        #n2 refers to the number of elements to scan
        n2 = n-x
        
        for x2 in range(n2-1):
        
            if (a[x]+a[x2+x+1])==k:
                
                Match.append([])
                Match[count].append(b[x])
                Match[count].append(b[x2+x+1])
                
                print "Match: %d, x: %d, x2: %d, p1: %d, p2: %d" % (count, a[x], a[x2+x+1], x, (x2+x+1))
                print "Match: %d, x: %d, x2: %d, p1: %d, p2: %d" % (count, Match[count][0], Match[count][1], x, (x2+x+1))
                count = count + 1
                break
                



a=[]
a.append(6)
a.append(0)
a.append(3)
a.append(46)
a.append(1)
a.append(3)
a.append(9)
a.append(6)
a.append(3)
a.append(3)
a.append(47)

numberOfPairs(a,6)

