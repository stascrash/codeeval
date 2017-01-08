import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	nums = test.split(",")
	num_set = (sorted(list(set([int(x) for x in nums]))))
	if len(num_set) == 1:
		print num_set[0]
	else:
		print (",".join([str(x) for x in num_set]))
test_cases.close()