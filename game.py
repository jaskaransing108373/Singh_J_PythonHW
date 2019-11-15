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

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose ", gameVars.computer, "\n")
	print("player chose ", player, "\n")

	### This is where you would have to call compare
	
	#### end compare stuff
	
	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]
