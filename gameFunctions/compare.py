from gameFunctions import gameVars

# What are you trying to compare inside de function? 
# you will need to pass those things in as arguments
# inside de round brackets
def comparechoices():
	if player == "quit":
		exit()
	elif gameVars.computer == player:
		print("tie! no one wins, play again")

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")