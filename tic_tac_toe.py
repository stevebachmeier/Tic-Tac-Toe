from intro import intro
from display_board import display_board
from place_marker import place_marker
from win_check import win_check
from choose_first import choose_first
from choose_symbol import choose_symbol
from full_board_check import full_board_check
from player_choice import player_choice
from replay import replay

intro()
while True:
	# Setup
	game_on = True
	board = ["#"," "," "," "," "," "," "," "," "," "]
	turn = int(choose_first())
	marker = choose_symbol(turn)
	marker1 = marker[0]
	marker2 = marker[1]
    
	# Play
	while game_on:
		# Player 1's turn
		if (turn == 1):
			position = player_choice(board,turn)
			place_marker(board, marker1, position)
			display_board(board)
			print("\n")
			if (win_check(board, marker1)):
				print(f"Congratulations Player {turn} - you won!")
				game_on = False
			else:
				if (full_board_check(board)):
					print("It's a draw!")
					break
				else:
					turn = 2
		# Player 2's turn
		else:
			position = player_choice(board,turn)
			place_marker(board, marker2, position)
			display_board(board)
			print("\n")
			if (win_check(board, marker2)):
				print(f"Congratulations Player {turn} - you won!")
				game_on = False
			else:
				if (full_board_check(board)):
					print("It's a draw!")
					break
				else:
					turn = 1
	if replay() == False:
		break