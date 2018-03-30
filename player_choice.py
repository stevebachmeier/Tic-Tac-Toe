def player_choice(board,turn):
	from space_check import space_check
	
	print(f"Player {turn}, you're up!")
	print("\n")
	
	while True:
		try:
			position = int(input("Choose an available board position: "))
		except ValueError:
			print("\n")
			print("Please input an integer (between 1-9): ")
			continue
			
		if (position not in range(1,10)):
			print("\n")
			print("Please choose an integer between 1-9: ")
			continue
		elif (space_check(board,position) == False):
			print("\n")
			print("That position is taken. Choose another: ")
			continue
		else:
			break
		
	return position