"""
Implement an autocomplete system. That is, given a query string s and a set of all possible
query strings, return all strings in the set that have s as prefix

For example, given the query string de and the set of strings[dog, deer, deal] return [deer, deal]
"""


# case sensitive
def complete_words_sen(prfx, words):
	result = []
	for word in words:
		if word[:len(prfx)] == prfx:
			result.append(word)

	return result


# and this one is not
def complete_words_ins(prfx, words):
	result = []
	for word in words:
		if word[:len(prfx)].lower() == prfx.lower():
			result.append(word)

	return result


def main():
	#Testing
	print(complete_words_sen('de', ['dog','deer','deal']))
	print(complete_words_ins('de', ['dog','deer','deal']))


if name == '__main__':
	main()
