"""
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the orginal array except
the one at i

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If out input was [3, 2, 1], the expected output would be [2, 3, 6]
"""

# using division
def mupl_array_values(arry):
	total = 1
	for i in arry:
		total *= i
	return [total//i for i in arry]


# without using division

def mupl_array_values_two(arry):
	res = [1] * len(arry)
	for idx, val in enumerate(arry):
		for i in range(len(res)):
			if i == idx:
				continue
			res[i] *= val

	return res


def mupl_array_values_three(arry):
	fwd = [1] * len(arry)
	bwk = [1] * len(arry)

	for idx in range(1, len(arry)):
		fwd[idx] = fwd[idx - 1] * arry[idx - 1]
		bwk[-idx - 1] = bwk[-idx] * arry[-idx]

	return [f * b for f, b in zip(fwd, bwk)]


def main():
	print(mupl_array_values([3, 2, 1]))
 	print(mupl_array_values([1, 2, 3, 4, 5]))
 	print(mupl_array_values_two([3, 2, 1]))
 	print(mupl_array_values_two([1, 2, 3, 4, 5]))
 	print(mupl_array_values_three([3, 2, 1]))
 	print(mupl_array_values_three([1, 2, 3, 4, 5]))


if __name__ == '__main__':
	main()
	