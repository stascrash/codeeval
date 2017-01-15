# https://www.codeeval.com/open_challenges/67/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('hex_to_decimal.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	print(int(test, 16))
test_cases.close()