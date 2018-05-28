from random import randint

def checkcows(number, guess):
	numdigits = list(str(number))
	guessdigits = list(str(guess))
	cows = 0
	size = len(numdigits)
	for digit in range(0,size):
		if numdigits[digit] == guessdigits[digit]:
			cows = cows + 1
	return cows

def checkbulls(numbers,guess):
	num= list(str(numbers))
	guess = list(str(guess))
	bulls = 0
	size = len(num)
	for i in range(0,size):
		for j in range(0,size):
			if i == j:
				break
			elif guess[i] == num[j]:
				bulls += 1
	return bulls	
	
def main():
	number = randint(1000,9999)

if __name__ == "__main__":
	main()
