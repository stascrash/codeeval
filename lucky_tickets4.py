import sys

def calcSums(maxsum, prevSums):
	results = []
	for s in range(0, maxsum + 1):
		result = 0
		for s1 in range(10):
			s2 = s - s1
			if s2 < 0:
				continue
			if s2 >= len(prevSums):
				continue
			result += prevSums[s2]
		results.append(result)
	return results


test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	ticketSize = int(test)
	sums = [1] * 10
	for n in range(2, (ticketSize / 2) + 1):
		maxSum = 9 * n
		sums = calcSums(maxSum, sums)
	result = 0
	for s in sums:
		result += s * s
	print(result)
test_cases.close()