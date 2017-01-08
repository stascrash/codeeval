import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	rolledLetters = ""
	count = 0
	for i in range(len(test)):
		letter = test[i]
		if letter.isalpha():
			if count == 0:
				rolledLetters += letter.upper()
			elif count % 2 != 0:
				rolledLetters += letter.lower()
			else:
				rolledLetters += letter.upper()
			count += 1

		else:
			rolledLetters += letter

	sys.stdout.write(rolledLetters)
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()