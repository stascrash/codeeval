import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	cleanLetters = []			
	for a in range(len(test)):
		symbol = test[a]
		if symbol.isalpha(): cleanLetters.append(symbol)
		else: cleanLetters.append(" ")
	tmpWord = "".join(cleanLetters).rstrip().lstrip().split(" ")
	cleanWords = []
	for word in tmpWord:
		if word != "":
			cleanWords.append(word)
	result = " ".join(cleanWords)
	print(result.lower())
test_cases.close()