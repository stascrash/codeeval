# https://www.codeeval.com/open_challenges/132/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('major_element.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	nums = test.split(',')
	half_length = len(nums) / 2
	major = 'None'
	val = max(set(nums), key=nums.count)
	if half_length < nums.count(val):
		major = val
	print(major)
test_cases.close()
