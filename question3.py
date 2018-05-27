def reverse(lst):
	rlist = lst[::-1]
	return rlist

def main():
	words = input("please enter a list")
	lst = words.split()
	rlst = reverse(lst)
	print(rlst)

if __name__ == "__main__":
	main()