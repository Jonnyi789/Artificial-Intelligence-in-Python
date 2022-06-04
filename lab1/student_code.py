import common
dRow = [0, 1, 0, -1]
dCol = [1, 0, -1, 0]

def df_search(map):
	found = False
	height = len(map)
	width = len(map[0])
	stack = []
	for y in range(height):
		for x in range(width):
			if map[y][x]==2:
				# map[y][x] = 4
				stack.append([(y,x)])
				break
		else:
			continue
		break
	final = []
	while stack:
		path = stack.pop()
		(y,x) = path[-1]
		if map[y][x]==3:
			found = True
			final = path
			break
		map[y][x] = 4
		for dd in range(4):
			newY = y + dRow[-1-dd]
			newX = x + dCol[-1-dd]
			if newY>=0 and newY<height and newX>=0 and newX<width:
				if map[newY][newX]==0 or map[newY][newX]==3:
					newPath = list(path)
					newPath.append((newY,newX))
					stack.append(newPath)
					
	if final:
		#path = stack.pop()
		for (y,x) in final:
			map[y][x] = 5
	return found

def bf_search(map):
	found = False
	height = len(map)
	width = len(map[0])
	queue = []
	for y in range(height):
		for x in range(width):
			if map[y][x]==2:
				map[y][x] = 4
				queue.append([(y,x)])
				break
		else:
			continue
		break
	while queue:
		path = queue.pop(0)
		(y,x) = path[-1]
		for dd in range(4):
			newY = y + dRow[dd]
			newX = x + dCol[dd]
			if newY>=0 and newY<height and newX>=0 and newX<width:
				if map[newY][newX]==0 or map[newY][newX]==3:
					newPath = list(path)
					newPath.append((newY,newX))
					queue.append(newPath)
					if map[newY][newX]==3:
						found = True
						break
					map[newY][newX] = 4
		else:
			continue
		break
	if queue:
		path = queue.pop()
		for (y,x) in path:
			map[y][x] = 5
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found
