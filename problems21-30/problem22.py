"""
Given a dictionary of worlds and a string made up of those words (no spaces), return
the orginal sentence in a list. If there is more than one possible reconstruction, return any 
of them. If there is no possible reconstruction, then return null

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox']

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond']
"""


def find_words(dicts, word):
	cache = 0
	rest = []
	for i in range(len(word)+1):
		if word[cache:i] in dicts:
			rest.append(word[cache:i])
			cache = i
	# cache = ' '.join(rest)

	return rest if len(' '.join(rest)) >= len(word) else None


def find_words_two(words, sentence):
	res = []

	while sentence:

		length = len(res)
		for word in words:
			if sentence.startswith(word):
				sentence = sentence[len(word):]
				res.append(word)

		if length == len(res):
			return None

	return res


def main():

	dictionary = ['quick', 'brown', 'the', 'fox']
	s = 'thequickbrownfox'

	dictionary1 = ['best', 'computer', 'lukasz', 'dom' ,'jest', 'portal' ,'best']
	s1 = 'lukaszjestthebest'

	print(find_words(dictionary, s))
	print(find_words(dictionary1, s1))
	print(find_words_two(dictionary, s))
	print(find_words_two(dictionary1, s1))


if __name__ == '__main__':
	main()
