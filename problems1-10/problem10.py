"""
Implement a job scheduler which takes in a function f and an integer n, and calls
f after n miliseconds
"""

from time import sleep

def scheduler(func, n):
	sleep(n/1000)
	return func();


def hallo():
	print("Hello")


def main():
	scheduler(hallo, 3)


if name == '__main__':
	main()