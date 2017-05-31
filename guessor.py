"""guessor.py by louis python, 2017 this program has user guessa number between 1 and 100."""

def main():
	# print "Guess a number between 1 and 100"
	# randomnumber = 35
	
	# 	userguess = input("Yor guess: ")
	# 	if userguess ==randomnumber:
	# 		print"You Got it"
	# 		found= true
	# 	elif userguess> randomnumber:
	# 		print "Guess lower"
	# 	else:
	# 		print"Guess high"
	
	print "Guess my number between 1 and 100"
	randomnumber = 35
	userguess = input("Your Number: ")
	if userguess == randomnumber:
		print "You Got It."
	else:
		print "Thats not it"


if __name__ == "__main__":
	main()