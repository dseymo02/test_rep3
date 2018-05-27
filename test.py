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
	assert prime(n) == True
