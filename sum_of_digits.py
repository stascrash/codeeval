import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	num_set = (int(test))
	a = num_set
	z = 0
	while (a != 0):
		z += a % 10
		a /= 10
	print z
test_cases.close()