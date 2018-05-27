import pytest
from question1, question2, question3, question4 import *

# test for q1

def testcheck():
	lst = [1,2,3,4,5,6,7]
	v = 3
	v2 = 8
	assert check(lst,v) == True
	assert check(lst,v2) == False
	