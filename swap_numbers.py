# https://www.codeeval.com/open_challenges/196/
import sys
test_lines = open(sys.argv[1], 'r')
test_cases = (line.rstrip() for line in test_lines)
# test_cases = ["4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5", "5Nobody5 7expects3 5the4 6Spanish4 9inquisition0"]

def swap(original_word):
	word = list(original_word)
	s = word[0]
	e = word[-1]
	word[0] = e
	word[-1] = s
	return "".join(word)


def main():
	for case in test_cases:
		words = case.split(" ")
		new_words = list()
		for word in words:
			new_words.append(swap(word))
		sys.stdout.write("{}\n".format(" ".join(new_words)))
		sys.stdout.flush()


if __name__ == '__main__':
	main()
