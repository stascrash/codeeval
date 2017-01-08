import sys
def isHappyNum(num):
	return num == 1

def getNumberOfDigits(num):
	return [int(x) for x in str(num)]

def getSquareRoot(num):
	return num * num

def getSumOfSquaredDigits(num):
	nums = getNumberOfDigits(num)
	result = 0
	for n in nums:
		result += getSquareRoot(n)
	return result


def main():
	test_cases = open(sys.argv[1], 'r')
	test_lines = (line.rstrip() for line in test_cases)
	for test in test_lines:
		happyNumber = False
		currentNum = int(test)
		stopLimit = 1000
		counter = 0
		while not happyNumber:
			counter += 1
			if counter > stopLimit:
				print("0")
				break

			currentNum = getSumOfSquaredDigits(currentNum)

			if isHappyNum(currentNum):
				print("1")
				happyNumber = True
	test_cases.close()

if __name__ == "__main__":
	main()