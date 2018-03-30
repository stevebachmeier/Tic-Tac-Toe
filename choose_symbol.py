def choose_symbol(turn):
	'''
	Prompts the randomly chosen first player to choose a symbol.
	'''
	marker = ""
	while ((marker != "X") and (marker != "O")):
		marker = input(f"Player {str(turn)}, choose 'X' or 'O': ").upper()
	if ((turn == 1) and (marker == "X")):
		print("\n")
		print("Ok, Player 1 is 'X' and Player 2 is 'O'!")
		print("\n")
		return("X","O")
	elif ((turn == 1) and (marker == "O")):
		print("\n")
		print("Ok, Player 1 is 'O' and Player 2 is 'X'!")
		print("\n")
		return ("O","X")
	elif ((turn == 2) and (marker == "X")):
		print("\n")
		print("Ok, Player 1 is 'O' and Player 2 is 'X'!")
		print("\n")
		return ("O","X")
	else:
		print("\n")
		print("Ok, Player 1 is 'X' and Player 2 is 'O'!")
		print("\n")
		return ("X","O")