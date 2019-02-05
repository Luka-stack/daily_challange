"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last
element of that pair.

For Example, car(cons(3, 4)) return 3, and cdr(cons(3, 4)) return 4
"""

# with inner function
def cons(a, b):
	def pair(f):
		return f(a,b)
	return pair


def car(pair):
	return pair(min)


def cdr(pair):
	return pair(max)


# without inner function
def cons1(a, b):
	return lambda f: f(a, b)


def car1(f):
	return f(lambda a, b: a)


def cdr1(f):
	return f(lambda a, b: b)



def main():
	print(car(cons(3,5)))
	print(cdr(cons(3,5)))

	print(car1(cons1(3,5)))
	print(cdr1(cons1(3,5)))


if __name__ == '__main__':
	main()