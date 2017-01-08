import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for line in test_lines:
	scramble = line
	words = scramble.split(";")[0].split()
	hints = [int(x) for x in scramble.split(";")[1].split()]
	hints_set = set([int(x) for x in scramble.split(";")[1].split()])
	words_num = set([(i + 1) for i in range(len(words))])
	missing_hint = list(hints_set ^ words_num)
	missing_hint = missing_hint[0]
	usedWordsIndex = []
	sorted_words = ["x"]*len(words)
	used_words = []

	for hint in hints:
		sorted_words[hint-1] = words[hints.index(hint)]
		usedWordsIndex.append(hints.index(hint))

	for item in usedWordsIndex:
		word = words[item]
		used_words.append(word)
	last_word = words[len(used_words):][0]
	sorted_words[missing_hint-1] = last_word
	deciphered_string = " ".join(sorted_words)
	print(deciphered_string)
test_cases.close()