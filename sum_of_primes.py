import sys
num = 2
all_primes = []
totalNumberOfPrimes = 0
def isPrime(num_check):
	if num_check > 1:
		for i in range(2, num_check - 1):
			if (num_check % i) == 0:
				return False
	return True
while totalNumberOfPrimes < 1000:
	if isPrime(num):
		all_primes.append(num)
		totalNumberOfPrimes += 1
	num += 1

sum_allprimes = sum(all_primes)
sys.stdout.write(str(sum_allprimes))
sys.stdout.flush()