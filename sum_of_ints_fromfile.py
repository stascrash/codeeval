import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
total = 0
for test in test_lines:
	total += int(test)
print(total)
test_cases.close()