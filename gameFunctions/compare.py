from gameFunctions import gameVars

# What are you trying to compare inside de function? 
# you will need to pass those things in as arguments
# inside de round brackets
def comparechoices():
	if player == "quit":
		exit()
	elif gameVars.computer == player:
		print("tie! no one wins, play again")

	elif player == "hot water":
		if gameVars.computer == "fire":
			print("You lose!", gameVars.computer, "extinguishes", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "colds", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "fire":
		if gameVars.computer == "ice":
			print("You lose!", gameVars.computer, "melts", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "extinguishes", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "ice":
		if computer == "hot water":
			print("You lose!", computer, "colds", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "melts", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")