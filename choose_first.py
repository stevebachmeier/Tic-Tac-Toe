def choose_first():
	import random
	first_player = str(random.randint(1,2))
	print(f"It has been randomly decided that player {first_player} goes first.")
	return first_player