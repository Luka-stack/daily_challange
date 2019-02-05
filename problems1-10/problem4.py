""""
Given an arry of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array
can contain duplicates and negative number as well

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

def contains(arry, num):
	for i in arry:
		if i == num:
			return True
	return False


def checkAllArry(arry):
	for i in range(len(arry)):
		if not contains(arry, i+1):
			return i+1
	return True


# in one function
def checkAllArryTwo(arry):
	tmp = [True] + [False] * len(arry)
	for el in filter(lambda x: 0 < x < len(arry), arry):
		tmp[el] = True
	return tmp.index(False)


def main():
	print(checkAllArryTwo([3, 4, -1, 1]))
	print(checkAllArry([1, 2, 0]))
	print(checkAllArry([3, 4, -1, 1]))
	print(checkAllArry([1, 2, 5]))
	print(checkAllArry([-1, 0, 6]))
	print(checkAllArry([100, 110, 116]))


if __name__ == '__main__':
	main()