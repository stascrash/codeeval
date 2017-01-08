import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
printed = ""
for test in test_lines:
	all_words = test.split(" ")
	good_words = []
	longest = ""
	longest_first = ""
	for word in all_words:
		word_letter = ""
		for letter in word:
			if not letter.isdigit():
				word_letter += letter
		if len(word_letter) > 0:
			good_words.append(word_letter)

	for i in good_words:
		if len(i) <= 10:
			longest = i
			idx = good_words.index(longest)

			for j in good_words:
				if len(j) > len(longest):
					longest = j
				elif len(j) == len(longest):
					if len(longest_first) == 0:
						longest_first = longest

	if printed != longest or printed != longest_first:
		if len(longest_first) != 0:
			to_print = longest_first
		else:
			to_print = longest

		for idx in range(len(to_print)):
			if idx == 0:
				sys.stdout.write(("*" * idx) + to_print[idx])
			else:
				sys.stdout.write(" " + ("*" * idx) + to_print[idx])
			sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.flush()
		printed = to_print
		longest_first = ""
test_cases.close()

#TODO: make counter for words of same length