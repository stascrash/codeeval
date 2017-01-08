import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

maxLength = 55
trimLine = 40
readMore = "... <Read More>"

for test in test_lines:
	if len(test) >= maxLength:
		trimmed = test[:trimLine].rstrip()
		trimmed += readMore
		test = trimmed
	print(test)
test_cases.close()