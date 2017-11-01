# https://www.codeeval.com/open_challenges/240/
import sys
from math import sqrt
test_lines = open(sys.argv[1], 'r')
test_cases = (line.rstrip() for line in test_lines)
mersenne_cache = dict()


def main():
	for case in test_cases:
		results = test(int(case))
		sys.stdout.write("{}\n".format(", ".join(results)))
		sys.stdout.flush()


def test(case_num):
	positives = list()
	for i in range(2, case_num):
		test_num = mersenne_num(i)
		if test_num:
			if test_num <= case_num:
				positives.append(str(test_num))
			else:
				break
	return positives


def mersenne_num(num):
	return cached(num)


def cached(num):
	cached_val = mersenne_cache.get(num, None)
	if not cached_val:
		if is_prime(num):
			val = 2 ** num - 1
			mersenne_cache[num] = val
			return val
	return cached_val


def is_prime(num):
	if num > 1:
		for i in range(2, int(sqrt(num)) + 1):
			if (num % i) == 0:
				return False
		return True
	return False


if __name__ == '__main__':
	main()
