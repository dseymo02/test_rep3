from random import randint

number = randint(1000,9999)

def checkcows(number, guess):
	list1 = []
	list2 = []
	list1.append([int(n) for n in number])
	list2.append([int(n) for n in guess])
	size = len(number)
	return list1
	
