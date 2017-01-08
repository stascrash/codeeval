directions = [(0, 1), (1, 0), (0,-1), (-1,0)]
sizex, sizey = 4, 4
dest = (2, 2)
pending_coords = (0,0)

cur_coords = (0,0)
cur_direction = 0
visited_map = []
for i in range(sizey): visited_map.append([False] * sizex)

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

nuts = 1
visited_map[0][0] = True

while True:
	direction = directions[cur_direction % 4]
	pending_coords = (cur_coords[0] +direction[0], cur_coords[1] + direction[1])
	print(pending_coords)

	if not checkCoords(pending_coords):
		print("Out of bounds")
		cur_direction += 1
		continue

	if visited_map[ pending_coords[0] ][ pending_coords[1] ]:
		print("Visited only")
		cur_direction += 1
		continue
	cur_coords = pending_coords
	visited_map[cur_coords[0]][cur_coords[1]] = True
	if cur_coords == dest:
		break
	nuts += 1


print nuts
print visited_map





