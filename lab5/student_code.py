import common
#import copy
#helpful, but not needed
class variables:
	counter=0

def solved(sudoku):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]==0:
				return False
	return True

def sudoku_backtracking(sudoku):
	variables.counter = 0
	#put your code here
	ans = bt(sudoku)
	return variables.counter
def bt(sudoku):
	variables.counter+=1
	if solved(sudoku):
		return True
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]==0:
				for ii in range(1,10):
					if common.can_yx_be_z(sudoku, y, x, ii):
						sudoku[y][x]=ii
						if bt(sudoku):
							return True
						sudoku[y][x] = 0	# num we tried didn't work
				if sudoku[y][x]==0:			# tried 1-9 yet none worked
					return False

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here
	domain = init_domain(sudoku)
	ans = fc(sudoku, domain)
	return variables.counter
def fc(sudoku, domain):
	variables.counter+=1
	if solved(sudoku):
		return True
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]==0:
				for ii in range(1,10):
					if common.can_yx_be_z(sudoku, y, x, ii):
						#dd = copy.deepcopy(domain)
						dd=[]
						for jj in range(9):
							newRow = list(map(list,domain[jj]))
							dd.append(newRow) 
						if let_yx_be_z(dd,y,x,ii):
							sudoku[y][x]=ii
							if fc(sudoku, dd):
								return True
							sudoku[y][x] = 0
				if sudoku[y][x]==0:
					return False
def init_domain(sudoku):
	dd=[]
	for y in range(9):
		row=[]
		for x in range(9):
			poss = list(range(1,10))
			row.append(poss)
		dd.append(row)
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]!=0:
				let_yx_be_z(dd,y,x, sudoku[y][x])
	return dd
def let_yx_be_z(domain,y,x,z):
	for line in range(9):
		if line!=x and (z in domain[y][line]):
			domain[y][line].remove(z)
			if not domain[y][line]:
				return False
		if line!=y and (z in domain[line][x]):
			domain[line][x].remove(z)
			if not domain[line][x]:
				return False
	curr_y = int(y/3)
	curr_x = int(x/3)
	for yy in range(curr_y*3, curr_y*3+3):
		for xx in range(curr_x*3, curr_x*3+3):
			if yy!=y and xx!=x and (z in domain[yy][xx]):
				domain[yy][xx].remove(z)
				if not domain[yy][xx]:
					return False
	return True