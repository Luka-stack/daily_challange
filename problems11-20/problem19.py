"""
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are
of the same color.

Given an N by K matrix where n-th row and k-th column represents the cost to build the n-th
house with k-th color, return the minimum cost which achieves this goal.
"""


def cheap_houses(matrix):
	total = 0
	a = 0
	for pr in matrix:
		pr.sort()
		total += pr[a:a+1][0]
		a = 1 if a == 0 else 0
	return total


def cheap_houses_two(matrix):
	return sum(sorted(val)[0] if idx % 2 == 0 else sorted(val)[1] for idx, val in enumerate(matrix))


def main():
	prices = [[10, 12, 11],
			  [14, 12, 10],
			  [11, 19, 18],
			  [11, 10,  9]]

	print(cheap_houses(prices))
	print(cheap_houses_two(prices))


if __name__ == '__main__':
	main()
	