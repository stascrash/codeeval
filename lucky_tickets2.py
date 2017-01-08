import sys
def generateNumber(numlen):
	return (pow(10, (numlen/2)) - 1)


# test_cases = open(sys.argv[1], 'r')
# test_lines = (line.rstrip() for line in test_cases)
test_lines = ["2","4","6","8"]
luck = 0
for test in test_lines:
	num_set = generateNumber(int(test))
	for n in range(num_set, 0, -1):
		a = n
		z = 0
		while (a != 0):
			z += a % 10
			a /= 10

		for x in xrange(num_set, 0, -1):
			b = x
			t = 0
			while (b != 0):
				t += b % 10
				b /= 10

			if z == t:
				luck += 1
	print(luck)
# test_cases.close()


