# https://www.codeeval.com/open_challenges/220/
import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open('trick_or_treat.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)
vampir_pts = 3
zombie_pts = 4
witch_pts = 5
for test in test_lines:
	data = test.split(',')
	vamp_num = int(data[0].split(':')[-1])
	zomb_num = int(data[1].split(':')[-1])
	witch_num = int(data[2].split(':')[-1])
	total_houses = int(data[3].split(':')[-1])

	total_kids = vamp_num + zomb_num + witch_num
	total_vamp_candies = vamp_num * total_houses * vampir_pts
	total_zomb_candies = zomb_num * total_houses * zombie_pts
	total_witch_candies = witch_num * total_houses * witch_pts

	all_candies = total_vamp_candies + total_zomb_candies + total_witch_candies
	for_each_candy = int(all_candies / total_kids)

	print(for_each_candy)