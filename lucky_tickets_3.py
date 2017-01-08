def generateNumber(numlen):
	return (pow(10, (numlen)) - 1)

def getSumOfNumSet(num_set_in):
	num_sum = 0
	for n in str(num_set_in):
		num_sum += int(n)
	return num_sum


def subset(nums, total, partial=[]):
	global sum_combos
	s = sum(partial)

	if s == total:
		return partial
	if s >= total:
		return

	for i in range(len(nums)):
		n = nums[i]
		remaining = nums[i+1:]
		a = subset(remaining, total, partial + [n])
		if a is not None:
			sum_combos.append(set(a))

num_set = generateNumber(4)
num_sum = getSumOfNumSet(num_set)
sum_combos = []
nums = [x for x in range(num_sum)]
subset(nums, num_sum)
print(sum_combos)

# match = 0
# for combo in sum_combos:
# 	if combo[0] == 0:
# 		tokenA = combo[1:]
# 		for x in sum_combos:
# 			if tokenA == x:
# 				match += 1
# 				# print "yes", x, combo

# print match
