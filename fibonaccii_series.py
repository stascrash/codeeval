import sys
'''
http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
fib(2) = 1
fib(1) = 1
fib(0) = 0
Therefore by substitution:
fib(3) = 1 + 1 + 0
'''
def fib(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	if n > 1:
		return fib(n - 1) + fib(n - 2)

test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)

for test in test_lines:
	print(fib(int(test)))
test_cases.close()