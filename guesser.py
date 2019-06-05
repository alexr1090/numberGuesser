#!/usr/bin/env python
import random

# Python guessing game
# Generates random number betwen 1 and 100 and 
# user to guess number. Will tell user if their guess
# is too high or too low or correct and then ask if
# they want to play again

def guessing(guess, number):
	"""
	Takes the correct number and the guess. 
	Compares guess to correct number and tells user
	whether their guess is correct, too high, or too low.
	This runs until the correct guess is found. error checks
	that guesses are valid integers. Also keeps list of guesses. 

	After correct guess is made displays users guesses and number 
	and asks user if they want to play again
	If they do returns true if they don't returns false.
	"""
	all_guesses= [str(guess)]
	while guess != number:
		if guess > number:	print "Sorry that is incorrect. The correct number is less than your guess."
		else: print "Sorry that is incorrect. The correct number is greater than your guess."
		valid = 0
		while not valid:
			try:
				guess=int(raw_input("What is your next guess?"))
				valid = 1
				all_guesses.append(str(guess))
			except ValueError:
				print ("Invalid number.")
	print ("Correct! It took you " + str(len(all_guesses)) + " guess(es) to guess correctly. Your guess(es) were/was " +  ", ".join(all_guesses))
	while True:
		try:	
			again = str(raw_input("Would you like to play again (y\\n)?").lower())
			if again != "n" and again != "y":
				raise ValueError("Incorrect")
			elif again == 'y': 
				return True
			else: 
				return False		
		except ValueError: 
		 	print "Please enter either y or n."

	 

def main():
	number = random.randint(1, 100)
	print("Hello, welcome to the guessing game!")
	again = True
	while again:
		all_guesses = []
		while 1:
			try:
				guess = int(raw_input("Please guess a number between one and one hundered. \n"))
			except ValueError:
				print ("Invalid number.")
				continue
			break
		again=guessing(guess,number)

	print "Thank you for playing. Good bye!"

if __name__ == '__main__':
	main()
