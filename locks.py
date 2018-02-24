"""
There are N unlocked rooms located in a row along the corridor.
A security guard, who starts the beat at the beginning of the corridor,
passes by and closes the lock of every second door (2nd, 4th, 6th…).
Then he returns to the beginning of the corridor, and passes by again
changing the state of every third door (3rd, 6th, 9th…) to the opposite
state — if the door is closed, security guard opens it; if the door is open, he closes it.

One iteration consists of two beats (when the security guard closes each second door,
and changes the state of each third door to the opposite state). The iteration repeats M-1 times.
During the last iteration, the security guard just changes the state of the last door in a row
(closes it, if the door is open or opens it, if the door is closed).

Your task is to determine how many doors have been left unlocked.

"""

import sys

# test_cases = open(sys.argv[1], 'r')
# test_lines = (line.rstrip() for line in test_cases)
test_lines = ["3 1", "100 100", "111 21"]

for test in test_lines:
	doors, loops = test.split(" ")
	doors = int(doors)
	loops = int(loops)
	doors_without_first = doors - 1
	if int(loops) == 1:
		print(doors_without_first)
	else:
		groups = doors_without_first // 6
		remains = doors_without_first - groups * 6
		open_doors = groups * 3 + 1
		if loops % 2 == 0:
			if remains != 4:
				open_doors += 1
		else:
			open_doors += groups
			if remains == 3:
				open_doors += 2
			elif remains != 2:
				open_doors += 1

		print(open_doors)
