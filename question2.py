def prime(n):
	result = "prime"
	for i in range(2,n):
		if n % i == 0:
			result = "not prime"
	return result
