import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	x, y, n = test.split(" ")
	x = int(x)
	y = int(y)
	n = int(n)

	for i in range(1, n + 1):
		if i % x == 0 and i % y == 0:
			print "FB",
		else:
			if i % x == 0:
				print "F",
			else:
				if i % y == 0:
					print "B",
				else:
					print i,
	print "\n"
test_cases.close()




