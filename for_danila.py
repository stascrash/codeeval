roadsize = 20
road = "_"*roadsize

train = "#-#-[]"
current_position = []
location = 1
def moveTrain():
	global location
	global current_position
	location = current_position.index(train) + 1

def updatePosition():
	global current_position
	global location
	for seg in range(roadsize):
		if seg == location:
			current_position.append(train)
			moveTrain()
		else:
			current_position.append(road[seg])

for x in range(10):
	updatePosition()
	print ("".join(current_position))
