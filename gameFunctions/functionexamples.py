# how to pass arguments into a function
#
def compareStuff(thing1, thing2):
	# compare and print all the things
	if thing1 == thing2:
		print('the match!')
	else:
		print('they do not match')


# invoke a Function by writting its name (calling it)
# and passing arguments

compareStuff('stuff', 'stuff')

compareStuff('stuff', 'other stuff')

compareStuff(1, 1)
compareStuff(1, 2)