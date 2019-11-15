from random import randint
from gameFunctions import gameVars

# define a python function that takes an argument
def winorlose(status): 
	# status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("************************")

	print("You", status + "! Would you like to play again?")

	choice = input("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		# this will break, currently - we will fix this next class
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.total_lives = 1
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]
	
	else:
		# use recursion to call winorlose again until we get the right input
		# recursion is just a fancy way to describe calling a function from within
		winorlose(status)