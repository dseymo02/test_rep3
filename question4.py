def printfib(n):
	seq = []
	for i in range(0,n):
		seq.append(fib(i))
	return seq

def fib(n):
	if n in [1,0]:
		return 1
	else:
		return fib(n-2) + fib(n-1)
