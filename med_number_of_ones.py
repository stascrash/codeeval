import sys

def get_bit(num, idx):
	return ((num & (1<<idx)) != 0)

test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	numOnes = 0
	a = int(test)
	for i in range(a.bit_length()):
		if get_bit(a, i):
			numOnes += 1
	print numOnes

test_cases.close()
