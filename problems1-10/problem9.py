"""
Given a list of integers, write a function that returns the largest sum of non-adjacent number.
Numbers can be 0 or negative

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6 and 5. [5, 1, 1, 5] should
return 10, since we pick 5 and 5
"""


# loop thru array and add non-adjacent numbers. Works exacly as porblem requires
def count_sum(arry):
	maxi = 0
	length = len(arry)
	for i in range(length//2):
		for start in range(2, length):
			for step in range(2, length):
				total = arry[i]
				for j in range(start, length, step):
					if i + j <= length - 1:
						total += arry[i+j]
					if i - j >= 0:
						total += arry[i-j]
				if total > maxi:
					maxi = total
	return maxi


# Works exacly as problem requires.
def count_sum_rec(arry):
	if not arry:
		return 0
	if len(arry) <= 2:
		return max(arry)

	# for [5, 1, 1, 5] -> [5, 1] + [5] (last)
	inc = count_sum_rec(arry[:-2]) + numbers[:-1]
	# for [5, 1, 1, 5] -> [5, 1]
	exc = count_sum_rec(arry[:-2])

	return max(inc, exc)


# loop thru array but add only these numbers which distant is 'step'
def count_sum_const(arry, step=2):
	maxi = 0
	length = len(arry)
	for i in range(length//2):
		total = arry[i]
		for j in range(step, length, step):
			if i + j <= length - 1:
				total += arry[i+j]
			if i - j >= 0:
				total += arry[i-j]
		if total > maxi:
			maxi = total

	return maxi


# loop thru arry but add only numbers where distance is incresing
def count_sum_inc(arry):
	maxi = 0
	length = len(arry)
	for i in range(length):
		total = arry[i]
		step = 0
		for j in range(2, length):
			if i + j + step <= length - 1:
				total += arry[i+j+step]
			if i - (j + step) >= 0:
				total += arry[i-(j + step)]
			step += j + 1
		if total > maxi:
			maxi = total

	return maxi



# testing
def main():
	print('count_sum')
	print(count_sum([2, 4, 6, 2, 5]))
	print(count_sum([5, 1, 1, 5]))
	print(count_sum([1, 2, 3, 4]))
	print(count_sum([2, 4, 6, 2, 5, 7]))
	print(count_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
	print('---')

	print('count_sum_const')
	print(count_sum_const([2, 4, 6, 2, 5]))
	print(count_sum_const([5, 1, 1, 5]))
	print(count_sum_const([2, 4, 6, 2, 5], 3))
	print(count_sum_const([5, 1, 1, 5], 3))
	print(count_sum_const([1, 9, 5, 3, 8, 5, 6, 0], 3))
	print(count_sum_const([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
	print('---')

	print('count_sum_inc')
	print(count_sum_inc([2, 4, 6, 2, 5]))
	print(count_sum_inc([5, 1, 1, 5]))
	print(count_sum_inc([1, 2, 3, 4, 5, 6, 7]))
	print(count_sum_inc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == '__main__':
	main()
