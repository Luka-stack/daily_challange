"""
The area of a cricle is defined as pir^2. Estimate pi to 3 decimal places using
Monte Carlo method

Hint: The basic equation of a circle is x^2 + y^2 = r^2

Note:
	The Idea is to generate random point (x, y) and plot it on square of 1u x 1u. And check if this
	point is inside Circle of R = 0.5u.

	We know that area of the square is 1 unit sq while that of cirlce is PI * (1/2)^2 = PI/4

	To sum up, we use equation:
	PI = 4 * number of points generated inside the circle / number of point generated inside the square
"""
from random import uniform


def estimate_pi(interval):
	# initialize circle and square points
	circle_points, square_points = 0, 0
	# initialize pi
	pi = 0

	for _ in range(interval):
		# generate random point x, y
		# Get a random number in the range [a, b) or [a, b] depending on rounding.
		rand_x, rand_y = round(uniform(0, 1.00), 3), round(uniform(0, 1.00), 3)
		# calculate d -> distance between x, y from the origin
		d = rand_x*rand_x + rand_y*rand_y

		# checkl if point (x, y) lies inside the define circle with R = 1
		if d <= 1:
			circle_points += 1

		# total number of points
		square_points += 1

		# estimate pi after each iteration
		pi = 4 * circle_points / square_points

		# output as a test for this solutionif
		if rand_x >= 1 or rand_y >= 1:
			print(f'(x:{rand_x}, y:{rand_y}) (CP:{circle_points}, SP:{square_points}) PI:{pi:.3f}')

	return pi


def main():
	print(f'Final Estimation Value for PI:{estimate_pi(5000):.3f}')


if __name__ == '__main__':
	main()