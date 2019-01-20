y = []

def MyConv(a,b):
	for i in range(0, len(a)+len(b)-1):
		y.append(0)

	for index in range(0, len(a)+len(b)-1):
		number = index
		y[index] = 0
	
		for index2 in range(0, len(b)):
			if(number>=0 and number<len(a)):
				y[index]=y[index]+(a[number]*b[index2])
	
			number = number-1
	return y
	
x = [2, 4, 6, 4, 2]
h = [3, -1, 2, 1]
print(MyConv(x,h))