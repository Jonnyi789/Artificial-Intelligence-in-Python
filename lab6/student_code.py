import common

def drone_flight_planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 
	y,x = find_end(map)
	values[y][x] = delivery_fee
	
	fires = find_fire(map)
	for y,x in fires:
		values[y][x] = 0-dronerepair_cost
	sy,sx = find_start(map)
	for iii in range(35):			#could converge earlier
		for y in range(6):
			for x in range(6):
				if map[y][x]<=1:
					curr=[]
					og = values[y][x]
					vs = bounce_value(values, og, y+1,x)
					vw = bounce_value(values, og, y,x-1)
					vn = bounce_value(values, og, y-1,x)
					ve = bounce_value(values, og, y,x+1)
					act1 = (vs*0.7+vw*0.15+ve*0.15)*discount - battery_drop_cost
					curr.append(act1)
					act2 = (vw*0.7+vs*0.15+vn*0.15)*discount - battery_drop_cost
					curr.append(act2)
					act3 = (vn*0.7+vw*0.15+ve*0.15)*discount - battery_drop_cost
					curr.append(act3)
					act4 = (ve*0.7+vs*0.15+vn*0.15)*discount - battery_drop_cost
					curr.append(act4)
					act5 = (vs*0.8+vw*0.1+ve*0.1)*discount - battery_drop_cost*2
					curr.append(act5)
					act6 = (vw*0.8+vs*0.1+vn*0.1)*discount - battery_drop_cost*2
					curr.append(act6)
					act7 = (vn*0.8+vw*0.1+ve*0.1)*discount - battery_drop_cost*2
					curr.append(act7)
					act8 = (ve*0.8+vs*0.1+vn*0.1)*discount - battery_drop_cost*2
					curr.append(act8)
					####
					values[y][x] = max(curr)
					dir = curr.index(values[y][x])+1 
					policies[y][x] = dir

	return values[sy][sx]

def bounce_value(value, og, y,x):
	if y<0 or x<0 or y==6 or x==6:
		return og
	else:
		return value[y][x]

def find_start(map):
	for y in range(6):
		for x in range(6):
			if map[y][x]==1:
				return y,x
def find_end(map):
	for y in range(6):
		for x in range(6):
			if map[y][x]==2:
				return y,x
def find_fire(map):
	fires=[]
	for y in range(6):
		for x in range(6):
			if map[y][x]==3:
				fires.append((y,x))
	return fires