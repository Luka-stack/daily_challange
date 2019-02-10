"""
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example. given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since
* 10 = max(10, 5, 2)
*  7 = max(5, 2, 7)
*  8 = max(2, 7, 8)	
*  8 = max(7, 8, 7)
"""


def count_length_test(array, k):
	for i in range(len(array) + 1 - k):
		print(f'* {max(array[i:i+k])} = max({array[i:i+k]})')


def count_length(array, k):
	return [max(array[i:i+k]) for i in range(len(array) + 1 - k)]


def main():
	test_arr = [10, 5, 2, 7, 8, 7]
	count_length_test(test_arr, 3)
	print(f'\n{count_length(test_arr, 3)}')


if __name__ == '__main__':
	main()
