import sys
def getLetterRepetitionCount(testPhrase):
	letterFrequency = {}
	for letter in testPhrase:
		if letter.isalpha():
			letter = letter.lower()
			if letter in letterFrequency.keys():
				letterFrequency[letter] += 1
			else:
				letterFrequency[letter] = 1
	return letterFrequency

def assignLetterPoints(lettersMap):
	availablePoints = 26
	gradedLetters = {}

	letters = list(lettersMap.keys())
	freqs = list(lettersMap.values())
	maxFreq = max(freqs)

	for i in reversed(range(1, maxFreq+1)):
		for f_Id in range(len(freqs)):
			f = freqs[f_Id]
			if i == f:
				a = letters[f_Id]
				if a not in gradedLetters.keys():
					gradedLetters[a] = availablePoints
					availablePoints -= 1
	return gradedLetters


def getMaxBeauty(letterPoints, testPhrase):
	result = 0
	for letter in testPhrase:
		if letter.isalpha():
			letter = letter.lower()
			result += letterPoints[letter]
	return result


def main():
	test_cases = open(sys.argv[1], 'r')
	test_lines = (line.rstrip() for line in test_cases)

	for test in test_lines:
		repetitionCount = getLetterRepetitionCount(test)
		letterPoints = assignLetterPoints(repetitionCount)
		maxBeauty = getMaxBeauty(letterPoints, test)
		print maxBeauty
	test_cases.close()

if __name__ == "__main__":
	main()


