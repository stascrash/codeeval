import sys

test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	word = test.split(" ")[0]
	code = test.split(" ")[1]
	codedword = ""

	for i in range(len(code)):
		if code[i] == "1":
			codedword += (word[i]).upper()
		else:
			codedword += word[i]
	sys.stdout.write(codedword)
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()



