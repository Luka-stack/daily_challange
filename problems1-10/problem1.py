"""
Given a list of numbers k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

"""

def add_to_k(arry, num):
	for i in arry:
		for j in arry:
			if i + j == num:
				return True
	return False


def add_to_k_two(arry, num):
	return  any(True for i in range(0, len(arry)) if (num - arry[i]) in arry[i+1:])
	#return (num - arry[i]) in arry[i+1:]) for i in range(0, len(arry))


def main():
	a = [10, 15, 3, 7]
	print(add_to_k_two(a, 17))
	print(add_to_k_two(a, 20))


if __name__ == '__main__':
	main()
