"""
Given a stream of elements too large to store in memory, pick a random element from
the stream with uniform probability.
"""


import random


def pick_random(large_stream):
	picked_element = None

	for idx, val in enumerate(large_stream):
		if random.randint(1, idx + 1) == 1:
			picked_element = val
		elif idx != 0:
			picked_element = val
