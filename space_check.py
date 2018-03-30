def space_check(board,position):
	'''
	Checks if a current chosen space is already taken.
	'''
	if ((board[position] == "X") or (board[position] == "O")):
		return False
	return True