# importing random library

import random

number = random.randint( 1, 100 )

# Number of chances for guessing the number. The chances for this game are 7.

chances = 0

print( 'What is your name?' )

a, b = input().split()

print( 'Hello {} {}! Lets play a game. '.format( a, b ) )

print( 'Guess the Number between 1 to 100' )

while ( chances < 7 ):
    
	guess = int( input() )

	if guess == number:

		print( 'Fabulous, You Won!!' )

		break

	elif guess < number:

		print( 'The guess was a bit Low. Guess a number higher than ', guess )

	else:

		print( 'The guess was a bit High. Guess a number lower than ', guess )

	chances += 1
	
		
# If all the chances are exhausted, then the user will lose the game. The ‘if not’ operator executes a block when the condition mentioned evaluates to False.

if not ( chances < 7 ):

    print( 'Sorry! You Lost. The number is ', number )



