import sys
for i in range(1, 100):
	if i % 2 > 0:
		sys.stdout.write(str(i))
		sys.stdout.write("\n")
		sys.stdout.flush()