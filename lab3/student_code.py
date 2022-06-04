import common
dRow = [0, 1, 0, -1]
dCol = [1, 0, -1, 0]
def astar_search(map):
	found = False
	height = len(map)
	width = len(map[0])
	order = []
	targetX = None
	targetY = None
	final = []
	for y in range(height):
		for x in range(width):
			if map[y][x]==3:
				targetX = x
				targetY = y
				break
		else:
			continue
		break
	for y in range(height):
		for x in range(width):
			if map[y][x]==2:
				#map[y][x] = 4
				order.append([(y,x,0, abs(targetX-x)+abs(targetY-y))])
				break
		else:
			continue
		break
	while order:
		path = order.pop()
		(y,x,g,h) = path[-1]
		if map[y][x]==3:
			found = True
			final = path
			break 
		map[y][x] = 4
		for dd in range(4):
			newY = y + dRow[dd]
			newX = x + dCol[dd]
			if newY>=0 and newY<height and newX>=0 and newX<width:
				if map[newY][newX]==0 or map[newY][newX]==3:
					newPath = list(path)
					newPath.append((newY, newX, g+1, abs(targetX-newX)+abs(targetY-newY)))
					order.append(newPath)
		order.sort(key = my_sort)
	if final:
		for (y,x,g,h) in final:
			map[y][x] = 5
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found
def my_sort(n):
	return (-n[-1][2]-n[-1][3], -n[-1][1], -n[-1][0])
