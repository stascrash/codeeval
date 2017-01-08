import sys
def isPrime(check_num):
	if check_num > 1:
		for i in range(2, check_num):
			if check_num % i == 0:
				return False
		return True

def isPalindrome(check_num):
	a = str(check_num)
	b = a[::-1]
	if a != b:
		return False
	return True

num = 0
palindrome_list = []
while num < 1000:
	if isPrime(num):
		if isPalindrome(num):
			palindrome_list.append(num)
	num += 1
sys.stdout.write(str(max(palindrome_list)))
sys.stdout.flush()
