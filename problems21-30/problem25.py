"""
Implement regular expression matching with the following special characters:
	- .(period) which matches any single character
	- *(asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression
and returns whether  or not the string matches the regular expression.
"""


def find_match(expr, templ):
	asterisk = False

	while expr and templ:

		if expr[0] == templ[0] or expr[0] == '.':
			templ = templ[1:]
			expr = expr[1:]
			asterisk = False
		elif expr[0] == '*':
			asterisk = True
			expr = expr[1:]
		elif expr[0] != templ[0] and asterisk:
			templ = templ[1:]
		else:
			return False

	if not expr and (not templ or asterisk):
		return True
	else:
		return False


def main():
	exp = '.*t'
	tmp = 'chat'
	print(f'Result:{find_match(exp, tmp)} Expect:True')

	exp = '.*t'
	tmp = 'chats'
	print(f'Result:{find_match(exp, tmp)} Expect:False')

	exp = 'ra.'
	tmp = 'ray'
	print(f'Result:{find_match(exp, tmp)} Expect:True')

	exp = 'ra.'
	tmp = 'raymond'
	print(f'Result:{find_match(exp, tmp)} Expect:False')

	exp = '.c*ray'
	tmp = '1cosray'
	print(f'Result:{find_match(exp, tmp)} Expect:True')

	exp = '.c*ray*'
	tmp = '1cosraymax'
	print(f'Result:{find_match(exp, tmp)} Expect:True')


	exp = '.c*ray'
	tmp = '1cosraymax'
	print(f'Result:{find_match(exp, tmp)} Expect:False')


if __name__ == '__main__':
	main()	
