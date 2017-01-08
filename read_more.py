# https://www.codeeval.com/open_challenges/167/
import sys
# test_cases = open(sys.argv[1], 'r')
test_cases = open('read_more.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)

maxLength = 55
trimLine = 40
readMore = "... <Read More>"

for test in test_lines:
	if len(test) > maxLength:
		trimmed = test[:trimLine]
		trimmed = trimmed.rsplit(' ', 1)[0] + readMore
		test = trimmed
	sys.stdout.write(test)
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()
