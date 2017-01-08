import sys
from datetime import time
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	allTimeTable = test.split(" ")
	timeSchedule = []
	sortedSchedule = []
	for timeEntry in allTimeTable:
		h, m, s = timeEntry.split(":")
		timeSchedule.append(time(int(h), int(m), int(s)))
	for timeEntry in reversed(sorted(timeSchedule)):
		formatedTime = timeEntry.strftime("%H:%M:%S")
		sortedSchedule.append(formatedTime)
	finalSchedule = " ".join(sortedSchedule)
	print finalSchedule
test_cases.close()