import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	testData = [float(x) for x in test.split(" ")]
	outPut = []
	for val in sorted(testData):
		val_str = "%.3f" % val
		outPut.append(val_str)
	out = " ".join(outPut)
	print(out)
test_cases.close()