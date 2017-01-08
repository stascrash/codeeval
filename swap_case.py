import sys
test_cases = open(sys.argv[1], 'r')
for sentence in test_cases:
	new_sentence = ""
	for letter in sentence:
		if letter.isalpha():
			if letter.isupper():
				letter = letter.lower()
				new_sentence += letter
			elif letter.islower():
				letter = letter.upper()
				new_sentence += letter
		else:
			new_sentence += letter
	print new_sentence
test_cases.close()
