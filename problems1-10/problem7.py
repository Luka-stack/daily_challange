"""
Given the mapping a = 1, b = 2, ... , z = 26, and an encoded message, count 
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', 'ak'

P.S.
prints are only for personal use :>
"""

# First code is wrong because I didn't understand the exercise xD
alf = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
		 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decode(code):
	# max code 999
	code = str(code)
	count = 0
	# divide on 2 and 1 elements np. 12 4 fail -> 11 0  check -> 99 9
	if code[2] != '0':
		if int(code[:2]) < 27:
			count += 1
			print(f"'{alf[int(code[:2])]}' '{alf[int(code[2])]}'")
		
	# divide on 1 and 2 elements np. 5 24 fail -> none check -> 9 99
	if int(code[1:]) < 27:
		count += 1 
		print(f"'{alf[int(code[0])]}' '{alf[int(code[1:])]}'")

	# divide on 3 elements np. 1 1 1 unless code contains '0'
	if '0' not in code:
		count += 1
		print(f"'{alf[int(code[0])]}' '{alf[int(code[1])]}' '{alf[int(code[2])]}'")

	return count;


# this one is correct
def decodeTwo(code):
	# working on numbers
	symbols = map(str, range(1, 27))
	if not code:
		return 1
	matches = filter(lambda symbol: code.startswith(symbol), symbols)
	encoded = [decodeTwo(code[len(m):]) for m in matches]
	
	return sum(encoded)


def main():
	print(decodeTwo('111'))
	print(decode(111))


if __name__ == '__main__':
	main()
