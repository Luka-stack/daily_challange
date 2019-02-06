"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function thath return the number of unique ways you can climb the staircase.
The order od the steps matters.
For example. if N is 4, then there are 5 unique ways:
* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being to climb 1 or 2 steps at a time, you could climb any number from a
set of positive integers X? For example. if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at at time.
"""


# first part
def climb_stair(length):
	ways = 1
	if length % 2 == 0:
		ways += 1
	tmp = length - 2
	if length > 0:
		ways += tmp + 1

	return ways


# second part first approach
def climb_stair_steps(length, steps):
	ways = 0
	for i in steps:
		if length % i == 0:
			ways += 1
	rem = length - sum(steps)
	tmp_ways = len(steps)
	if rem == 0:
		return ways + tmp_ways
	while rem >= min(steps):
		if rem in steps:
			return ways + tmp_ways + 1
		rem -= min(steps)
		tmp_ways += 1

	return ways


# second part with recursion
def climb_stair_rec(length, steps):
	if length == 0:
		return 1
	# check if steps isn't bigger than length
	choices = [s for s in steps if s <= length]
	# no choices to possible movement
	if not choices:
		return 0
	count = 0
	for c in choices:
		count += climb_stair_rec(length - c, steps)

	return count


def main():
	print(climb_stair(2))
	print(climb_stair(4))
	print(climb_stair(5))
	print(climb_stair_steps(10, [2, 5]))
	print(climb_stair_steps(12, [2, 5]))
	print(climb_stair_steps(14, [2, 5]))
	print(climb_stair_rec(4, [1, 2]))
	print(climb_stair_rec(14, [2, 5]))


if __name__ == '__main__':
	main()
