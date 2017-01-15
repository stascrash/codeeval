# https://www.codeeval.com/open_challenges/103/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('lowest_unique_number.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	unique = list()
	nums = list(map(int, test.split(' ')))
	for num in nums:
		if nums.count(num) == 1:
			unique.append(num)
	try:
		min_unque = min(unique)
		print(nums.index(min_unque) + 1)
	except ValueError:
		print(0)
test_cases.close()

