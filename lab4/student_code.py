import common

def minmax_tictactoe(board, turn):
	#put your code here:
	if turn==common.constants.X:
		return min_value(board)
	else:
		return max_value(board)
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

def max_value(board):	#O's mind, 2>0>1
	curr = common.game_status(board)
	if curr>0:
		return curr
	vv = 0
	for y in range(3):
		for x in range(3):
			if common.get_cell(board,y,x)==0:
				newBoard = list(board)
				common.set_cell(newBoard,y,x,2)
				vv = max(vv, abs(min_value(newBoard)-0.75))
				# 0.75 specifically picked to avoid floats accuracy problem like 0.8
	return change_back(vv)
def min_value(board):	#X's mind, 1>0>2
	curr = common.game_status(board)
	if curr>0:
		return curr
	vv = 2.75
	for y in range(3):
		for x in range(3):
			if common.get_cell(board,y,x)==0:
				newBoard = list(board)
				common.set_cell(newBoard,y,x,1)
				vv = min(vv, abs(max_value(newBoard)-0.75))
				# print(vv)
	return change_back(vv)

def change_back(num):
	#print("A") if a > b else print("=") if a == b else print("B")
	return 1 if num==0.25 else 2 if num==1.25 else 0 

def abprun_tictactoe(board, turn):
	#put your code here:
	if turn==common.constants.X:
		return min_abp(board,0,2.75)
	else:
		return max_abp(board,0,2.75)
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

def max_abp(board,aa,bb):
	curr = common.game_status(board)
	if curr>0:
		return curr
	vv = 0
	for y in range(3):
		for x in range(3):
			if common.get_cell(board,y,x)==0:
				newBoard = list(board)
				common.set_cell(newBoard,y,x,2)
				vv = max(vv, abs(min_abp(newBoard,aa,bb)-0.75))
				if vv>=bb:
					return change_back(vv)
				aa = max(aa, vv)
	return change_back(vv)
def min_abp(board,aa,bb):
	curr = common.game_status(board)
	if curr>0:
		return curr
	vv = 2.75
	for y in range(3):
		for x in range(3):
			if common.get_cell(board,y,x)==0:
				newBoard = list(board)
				common.set_cell(newBoard,y,x,1)
				vv = min(vv, abs(max_abp(newBoard,aa,bb)-0.75))
				if vv<=aa:
					return change_back(vv)
				bb = min(bb, vv)
	return change_back(vv)