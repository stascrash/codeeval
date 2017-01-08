import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	num = int(test)
	if num % 2 == 0:
		sys.stdout.write("1")
		sys.stdout.write("\n")
		sys.stdout.flush()
	else:
		sys.stdout.write("0")
		sys.stdout.write("\n")
		sys.stdout.flush()
test_cases.close()