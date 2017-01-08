import sys

def getNumSum(num):
	num_sum = 0
	for n in num:
		num_sum += int(n)
	return num_sum

def isLucky(numstr):
	left_set = numstr[:numlen/2]
	right_set = numstr[numlen/2:]
	return getNumSum(left_set) == getNumSum(right_set)

def generateSTRnum(num, numlen):
	return ("0" * ( numlen - len(str(num))) + str(num))



test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)


for test in test_lines:
	numlen = int(test)
	lucky = 0
	startNum = 0
	while len(str(startNum)) <= numlen:
		if isLucky(generateSTRnum(startNum, numlen)):
			lucky += 1
		startNum += 1
	print(lucky)
	#print "time to get %s: %0.2f \n" % (test, (end-start))
		

test_cases.close()


