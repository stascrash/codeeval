'''
Given a number n and two integers p1,p2 determine
if the bits in position p1 and p2 are the same or not.
Positions p1 and p2 are 1 based.
sample:
86,2,3
125,1,2
'''
import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	num, p1, p2 = (int(x) for x in test.split(","))
	binnum = bin(num).split("b")[1]
	if (binnum[len(binnum) - p1]) == (binnum[len(binnum) - p2]):
		sys.stdout.write("true")
		sys.stdout.write("\n")
		sys.stdout.flush()
	else:
		sys.stdout.write("false")
		sys.stdout.write("\n")
		sys.stdout.flush()
test_cases.close()