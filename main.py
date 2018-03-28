largest, index = 0, -1
for n in range(1,1000000):
	count = 0
	tmp = n
	while (n>1):
		if(n%2 == 0):
			n = n/2
		else:
			n = 3*n + 1
		count = count + 1
	if(count>largest):
		largest = count
		index = tmp+1
print("Largest count is %i for number %i"%(largest,index))