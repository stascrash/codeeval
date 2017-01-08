import sys
def checkCoords(coords):
	if coords[0] < 0:
		return False
	if coords[1] < 0:
		return False
	if coords[0] >= sizey:
		return False
	if coords[1] >= sizex:
		return False
	return True

# test_cases = open(sys.argv[1], 'r')
# test_lines = (line.rstrip() for line in test_cases)
if __name__ == "__main__":

	test_lines = ["4x4 | 3 3"]#,"4x4 | 3 3"]#, "20x30 | 2 3"]
	for test in test_lines:
		directions = [(0, 1), (1, 0), (0,-1), (-1,0)]
		sizex = int(test.split("|")[0].split("x")[0])
		sizey = int(test.split("|")[0].split("x")[1])
		desty = int(test.split("|")[1].strip().split(" ")[0])
		destx = int(test.split("|")[1].strip().split(" ")[1])
		dest = (destx-1, desty-1)
		
		pending_coords = (0,0)
		cur_coords = (0,0)
		cur_direction = 0
		visited_map = []
		nuts = 1
		for i in range(sizey): visited_map.append([False] * sizex)
		visited_map[0][0] = True

		while True:
			direction = directions[cur_direction % 4]

			pending_coords = (cur_coords[0] + direction[0], cur_coords[1] + direction[1])

			checkCoords(pending_coords)

			if not checkCoords(pending_coords):
				# print "False", "->", pending_coords
				cur_direction += 1
				continue
			if visited_map[ pending_coords[0] ][ pending_coords[1] ]:
				# print "Visited", "->", pending_coords
				cur_direction += 1
				continue
			cur_coords = pending_coords
			visited_map[cur_coords[0]][cur_coords[1]] = True
			# for x in visited_map:
			# 	print x
			# print "------------"
			if cur_coords == dest:
				break
			nuts += 1


		sys.stdout.write(str(nuts))
		sys.stdout.write("\n")
		sys.stdout.flush()

	# test_cases.close()
	#Using a different Python interpreter