import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	words = test.split(" ")
	for word in words:
		fixed_word = ""
		w_id = words.index(word)
		if word[0].isalpha():
			fixed_word = word[0].upper()
		else:
			fixed_word = word[0]
		fixed_word += word[1:]
		words[w_id] = fixed_word
	print(" ".join(words))
test_cases.close()