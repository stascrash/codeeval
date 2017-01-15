# https://www.codeeval.com/open_challenges/104/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('word_to_digit.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)
word_map = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
for test in test_lines:
	words = test.split(';')
	num = "".join([str(word_map[x]) for x in words])
	print(num)
test_cases.close()

