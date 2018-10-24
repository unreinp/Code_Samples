
def findMults(num1,num2,rangemax):
	x = num1
	y = num2
	while x < rangemax:
		x += num1
		print(x)
	while y < rangemax:
		y += num2
		print(y)
	return x+y
dog = findMults(5,3,10)

print ('the sum of all multiples of 5 and 3 between 0 and 1000: ' + str(dog))

