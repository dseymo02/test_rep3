import pytest
from question1 import *
from question2 import *
from question3 import *
from question4 import *
from question5 import *
from question6 import *

# test for q1

def testcheck():
	lst = [1,2,3,4,5,6,7]
	v = 3
	v2 = 9
	assert check(lst,v) == True
	assert check(lst,v2) == False

# test for q2

def testprime():
	n = 3
	n2 = 4
	assert prime(n) == "prime"
	assert prime(n2) == "not prime"

# test for q3

def reverse():
	lst = ["he", "is", "doing", "okay"]
	assert reverse(lst) == ["okay", "doing", "is", "he"]

# test for q4
def testprintfib():
	number = 5
	assert printfib(number) == [1,1,2,3,5]

# test for q5
def testintersection():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	assert intersection(a,b) == [1,2,3,5,8,13]

# test for q6
def testcheck():
	number = "1277"
	guess1 = "1234"
	guess2 = "1526"
	assert checkcows(number, guess1) == "2 cows"
	assert checkcows(number, guess2) == "1 cow"

