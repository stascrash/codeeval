import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	nums = test.split(";")
	num_set_a = set([int(x) for x in nums[0].split(",")])
	num_set_b = set([int(x) for x in nums[1].split(",")])
	num_set_c = sorted(list(num_set_a & num_set_b))

	if len(num_set_c) == 0:
		print "\n"
	if len(num_set_c) == 1:
		print num_set_c[0]
	else:
		print (",".join([str(x) for x in num_set_c]))
test_cases.close()