from show_board_positions import show_board_positions

def intro():
	'''
	Welcomes the players and calls the reference board layout.
	'''
	print("\n"*100)
	print("Welcome to Tic-Tac-Toe!")
	print("\n")
	print("For your reference, this is the board layout:")
	
	show_board_positions()
	print("\n")