import sys
import math
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	points = test.split(") (")
	ptA = points[0].lstrip("(").rstrip(")")
	ptB = points[1].lstrip("(").rstrip(")")
	ptA = tuple([int(x) for x in ptA.split(", ")])
	ptB = tuple([int(x) for x in ptB.split(", ")])
	#a^2 + b^2 = c^2
	horizontal_side =ptA[0] - ptB[0]
	vertical_side = ptA[1] - ptB[1]
	hypotenuse = int(math.sqrt((horizontal_side*horizontal_side + vertical_side*vertical_side)))
	print(hypotenuse)
test_cases.close()




