import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	total = int(test)
	new_total = 0
	remain = 0
	coin_total = 0
	c_current = 0
	c1, c2, c3 = 1, 3, 5
	new_total = total
	while new_total > 0:
		if new_total >= c3:
			c_current = new_total / c3
			coin_total += c_current
			new_total = new_total - (c_current * c3)

		if new_total >= c2:
			c_current = new_total / c2
			coin_total += c_current
			new_total = new_total - (c_current * c2)

		if new_total >= c1:
			c_current = new_total / c1
			coin_total += c_current
			new_total = new_total - (c_current * c1)
	print(coin_total)
test_cases.close()
#OR use this one liner
	#coin_total = (total / 5) + ((total % 5) / 3) + ((total % 5) % 3)