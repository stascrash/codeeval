# '''
# Given a number n and two integers p1,p2 determine
# if the bits in position p1 and p2 are the same or not.
# Positions p1 and p2 are 1 based.
# sample:
# 86,2,3
# 125,1,2
# '''
# import sys
# test_cases = open(sys.argv[1], 'r')
# test_lines = (line.rstrip() for line in test_cases)
# for test in test_lines:
# 	num, p1, p2 = (int(x) for x in test.split(","))
# 	binnum = bin(num).split("b")[1]
# 	if (binnum[len(binnum) - p1]) == (binnum[len(binnum) - p2]):
# 		sys.stdout.write("true")
# 		sys.stdout.write("\n")
# 		sys.stdout.flush()
# 	else:
# 		sys.stdout.write("false")
# 		sys.stdout.write("\n")
# 		sys.stdout.flush()
# test_cases.close()

import sys


def checkBits(num, bit):
    bit -= 1
    mask = 1 << bit
    result = num & mask
    return result >> bit


# test_cases = open(sys.argv[1], 'r')
# test_lines = (line.rstrip() for line in test_cases)
test_lines = ["86,2,3", "125,1,2", "1,63,50"]
for test in test_lines:
    num, p1, p2 = (int(x) for x in test.split(","))
    if checkBits(num, p1) == checkBits(num, p2):
        sys.stdout.write("true")
        sys.stdout.write("\n")
        sys.stdout.flush()
    else:
        sys.stdout.write("false")
        sys.stdout.write("\n")
        sys.stdout.flush()
# test_cases.close()
