"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example. given [(30, 75), (0, 50), (60, 150)], you should return 2
"""


def count_classes(intervals):
	data = [0]

	for itr in sorted(intervals):
		data.sort()
		if itr[0] >= data[0]:
			data.pop(0)
		data.append(itr[1])

	return len(data)


def main():
	intervals = [(70, 150), (30, 35), (0, 50), (25,29), (32, 75)]
	print("We need at least: {} classes".format(count_classes(intervals)))
	print("We need at least: {} classes".format(count_classes([(30, 75), (0, 50), (60, 150)])))


if __name__ == '__main__':
	main()
