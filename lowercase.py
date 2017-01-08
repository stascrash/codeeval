import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	sys.stdout.write(test.lower())
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()