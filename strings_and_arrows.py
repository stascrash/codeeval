import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
arrows = [">>-->", "<--<<"]
grab_set = len(arrows[0])

for test in test_lines:
	fullMatchInLine = 0
	for i in range(len(test)):
		max_len = len(test)
		if not i + grab_set > max_len:
			part = test[i:i+grab_set]
			if part == arrows[0] or part == arrows[1]:
				fullMatchInLine += 1
	sys.stdout.write(str(fullMatchInLine))
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()


