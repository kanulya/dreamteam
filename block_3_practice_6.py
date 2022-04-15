numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
a = [int(i) for i in numbers]
for i in range(1, len(a)):
	if a[i] > a[i - 1]:
        	print(a[i])
