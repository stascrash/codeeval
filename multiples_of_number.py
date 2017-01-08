import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	nums = test.split(",")
	x = int(nums[0])
	n = int(nums[1])
	multiple = 0
	counter = 0
	while multiple <= x:
		multiple = counter * n
		counter += 1

	if multiple & 1 == 0:
		sys.stdout.write(str(multiple))
		sys.stdout.write("\n")
		sys.stdout.flush()

test_cases.close()