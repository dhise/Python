import sys
import random


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def game():
	winning = False
	number = random.randint(num1, num2)
	while winning == False:
		guess = int(input(f'Guess a number between {num1} and {num2} '))
		if guess > number:
			print('Too high!')
		elif guess < number:
			print('Too low!')
		else:
			print('Nice you got it!')
			winning = True
		
game()
