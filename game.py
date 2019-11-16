# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

while gameVars.player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", gameVars.computer_lives, "/", gameVars.total_lives, "\n")
	print("Player lives: ", gameVars.player_lives, "/", gameVars.player_lives, "\n")
	print("Choose your weapon!\n")
	print("**********************************")

	player = input("choose hot water, ice or fire: ")
	player = player.lower()

	print("computer chose ", gameVars.computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit": 
		exit()
	elif gameVars.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "hot water":
		if gameVars.computer == "fire":
			print("You lose!", gameVars.computer, "extinguishes", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "colds", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1 

	elif player.lower() == "fire":
		if gameVars.computer == "ice":
			print("You lose!", gameVars.computer, "melts", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "extinguishes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1 

	elif player.lower() == "ice":
		if gameVars.computer == "hot water":
			print("You lose!", gameVars.computer, "colds", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "melts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")


	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]
