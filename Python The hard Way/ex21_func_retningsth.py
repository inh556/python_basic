def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a +b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLY %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDE %d / %d" % (a,b)
	return a / b
	
print "Let's do some math with just functions"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ:%d" %(age, height,weight,iq)

what = add(age,subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

value1 = divide(iq,2)
value2 = multiply(weight, value1)
value3 = subtract(height, value2)
what = add(age, value3)

print what
