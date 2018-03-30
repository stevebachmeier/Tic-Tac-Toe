def full_board_check(board):
	'''
	Checks if every board space has been played.
	'''
	i = 1
	while i < 9:
		if ((board[i] != "X") and (board[i] != "O")):
			return False
			break
		i += 1
	return True