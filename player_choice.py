def player_choice(board,turn):
	from space_check import space_check
	
	# position = int(input(f"Player {turn}, you're up! Choose an available board position: "))
	# while ((position not in range(1,10)) or (space_check(board,position) == False)):
		# if ((position not in range(1,10)) or (isinstance(position,int) == False)):
			# position = int(input("Must choose an integer between 1-9. Try again: "))
			# continue
		# elif (space_check(board,position) == False):
			# position = int(input("That position is taken. Try again: "))
			# continue
	# return position
	
	print(f"Player {turn}, you're up!")
	
	while True:
		try:
			print("\n")
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