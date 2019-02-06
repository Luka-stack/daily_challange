"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters

For example. given s = 'abcba' and k = 2, the longest substring with k distinct characters is 'bcb'
"""
from collections import Counter


# it returning string
def longest_substring(k, s):
	longest = ''
	for i in range(len(s))
		if len(Counter(s[i:])) == k:
			if len(s[i:]) > len(longest):
				longest = s[i:]
		if len(Counter(s[:-i])) == k:
			if len(s[:-i]) > len(longest):
				longest = s[:-i]
		if len(Counter(s[i:-i])) == k:
			if len(s[i:-i]) > len(longest):
				longest = s[i:-i]

	return longest


# and this one is working fine with problem
def longest_substring_two(k, s):
	longest = k
	for st_id in range(len(s)):
		ed_id = len(s)
		while True:
			dist = len(set(s[st_id:ed_id]))
			if dist <= k:
				break
			ed_id -= 1
		longest = max(longest, ed_id - st_id)

	return longest



def main():
	print(longest_substring(2, 'abcba'))
	print(longest_substring(2, 'abcdcba'))
	print(longest_substring(2, 'aabcd'))
	print(longest_substring(3, 'aaabbbcccddd'))
	print(longest_substring_two(2, 'abcba'))
	print(longest_substring_two(2, 'abcdcba'))
	print(longest_substring_two(2, 'aabcd'))
	print(longest_substring_two(3, 'aaabbbcccddd'))


if __name__ == '__main__':
	main()
