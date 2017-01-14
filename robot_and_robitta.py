# https://www.codeeval.com/open_challenges/212/
import sys
import re


def count(m, n, x, y):
	nuts = 0
	while n > y:
		mt, nt, xt, yt = m, n, x, y
		nuts = nuts + mt
		m = nt - 1
		n = mt
		x = nt - yt
		y = xt
	return nuts + x

if __name__ == "__main__":
	# test_cases = open(sys.argv[1], 'r')
	# test_lines = (line.rstrip() for line in test_cases)
	test_lines = ["4x4 | 3 3", "3x2 | 2 1"]#, "20x30 | 2 3", "45x50 | 40 25"]
	for test in test_lines:
		m, n, x, y = map(int, re.findall(r'\d+', test))
		nuts = count(m, n, x, y)
		sys.stdout.write(str(nuts))
		sys.stdout.write("\n")
		sys.stdout.flush()
	# test_cases.close()