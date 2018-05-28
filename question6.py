from random import randint

number = randint(1000,9999)

def checkcows(number, guess):
	numdigits = list(str(number))
	guessdigits = list(str(guess))
	cows = 0
	size = len(numdigits)
	for digit in range(0,size):
		if numdigits[digit] == guessdigits[digit]:
			cows = cows + 1
	return cows
	
	
