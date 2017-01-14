# https://www.codeeval.com/open_challenges/220/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('self_describing_numbers.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)