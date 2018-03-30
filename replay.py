def replay():
	'''
	Asks the players if they would like to play again.
	'''
	prompt = ""
	while ((prompt.upper() != "Y") and (prompt.upper() != "N")):
		prompt = input("Would you like to play again (y/n)? ")
	return prompt.upper() == "Y"