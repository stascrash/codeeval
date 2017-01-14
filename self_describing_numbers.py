# https://www.codeeval.com/open_challenges/40/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('self_describing_numbers.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	success = 1
	for pos, val in enumerate(test):
		if int(val) != test.count(str(pos)):
			success = 0
	sys.stdout.write(str(success))
	sys.stdout.write("\n")
	sys.stdout.flush()
