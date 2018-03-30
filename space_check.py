def space_check(board,position):
	if ((board[position] == "X") or (board[position] == "O")):
		return False
	return True