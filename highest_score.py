import sys
test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
	tbl_row_clean = []
	tbl_rows_dirty = test.split("|")
	maxscore = []
	number_categor = 0
	for scoreset in tbl_rows_dirty:
		score = ([int(x) for x in scoreset.lstrip().rstrip().split(" ")])
		number_categor = len(score)
		tbl_row_clean.append(score)
		
	for i in range(number_categor):
		reorder = []
		for j in tbl_row_clean:
			reorder.append(j[i])
		maxscore.append(reorder)

	for x in maxscore:
		sys.stdout.write(str(max(x)))
		sys.stdout.write(" ")
		sys.stdout.flush()
	sys.stdout.write("\n")
	sys.stdout.flush()
test_cases.close()