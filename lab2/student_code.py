QUEENS = 10

def gradient_search(board):
	found = False
	curr = attacking_queens(board)
	# local_minima changes the board if a lower is found
	changed = local_minima(board) # a diff board from last line now
	while curr > changed:
		curr = attacking_queens(board)
		changed = local_minima(board)
	if changed==0: 
		found = True
	return found

def attacking_queens(board):
	curr = 0
	for x in range(QUEENS):
		for y in range(QUEENS):
			if board[y][x]==1:
				#attack = []
				col = x+1
				while col<QUEENS:
					if board[y][col]==1:
						curr+=1
					col+=1
				col = x+1
				row = y-1
				while col<QUEENS and row>=0:
					if board[row][col]==1:
						curr+=1
					col+=1
					row-=1
				col = x+1
				row = y+1
				while col<QUEENS and row<QUEENS:
					if board[row][col]==1:
						curr+=1
					col+=1
					row+=1
				break
	return curr

def local_minima(board):
	mini = attacking_queens(board)
	changeThisX = None
	changeThisY = None
	changeIntoY = None
	for x in range(QUEENS):
		queen_row = 0
		while board[queen_row][x] != 1:
			queen_row+=1
		board[queen_row][x] = 0
		for y in range(QUEENS):
			board[y][x] = 1
			swapped = attacking_queens(board)
			if swapped < mini:
				mini = swapped
				changeThisX = x
				changeThisY = queen_row
				changeIntoY = y
			board[y][x] = 0
		board[queen_row][x] = 1
	if changeThisX != None:
		board[changeThisY][changeThisX] = 0
		board[changeIntoY][changeThisX] = 1
	return mini