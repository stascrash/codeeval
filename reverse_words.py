import sys

test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	if len(test) != 0:
		text_line = test.split(" ")
		out_text = " ".join(reversed(text_line))
		print out_text
test_cases.close()