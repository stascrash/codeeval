##i.isalpha()
##i.isdigit()
import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
#test_lines = ["abcdefghik", "Xa,}A#5N}{xOBwYBHIlH,#W", "(ABW>'yy^'M{X-K}q,", "6240488"]
char_map = [x for x in "abcdefghij"]

for test in test_lines:
	out_text = ""
	for symbol in test:
		if symbol.isalpha():
			try:
				idx = char_map.index(symbol)
				out_text += str(idx)
			except ValueError:
				pass
		if symbol.isdigit():
			out_text += str(symbol)
	if out_text == "":
		out_text = "NONE"
	print out_text








