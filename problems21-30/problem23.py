"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coodrinate from the start. If there is no possible path, then return null.
You can move up, left, down and right. You cannot move through walls. You cannot wrap around the 
edges of the board.

For example. given the following board:
[
	[f, f, f, f],
	[t, t, f, t],
	[f, f, f, f],
	[f, f, f, f]
]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps
required to each the end is 7, since we would need go through (1, 2) because there is a wall
everywhere else on the second row.
"""


def calc_fast_route(maze, start, end):
	valid_coords = [(row, col) for row, val_row in enumerate(maze)
					for col, val_col in enumerate(maze[row]) if val_col == False] 

	mapped = [[None for _ in range(len(maze[i]))] for i in range(len(maze))] 
	current_distance = 0
	mapped[start[0]][start[1]] = current_distance

	while True:
		coords = [coord for coord in valid_coords if mapped[coord[0]][coord[1]] == current_distance]
		if not coords:
			break

		current_distance += 1
		for c in coords:
			neighbours = [coord for coord in valid_coords if abs(coord[0] - c[0]) + abs(coord[1] - c[1]) == 1]
			for n in neighbours:
				if mapped[n[0]][n[1]] == None:
					mapped[n[0]][n[1]] = current_distance

	return mapped[end[0]][end[1]]


def main():

	matrix = [[False, False, False, False],
			  [True , True , False, True ],
			  [False, False, False, False],
			  [False, False, False, False]]

	matrix2 = [[False, False, False, False],
			   [True , True , True , True ],
			   [False, False, False, False],
			   [False, False, False, False]]

	start = (3, 0)
	end = (0, 0)

	# Testing Output
	print(calc_fast_route(matrix, start, end))
	print(calc_fast_route(matrix2, start, end))


if __name__ == '__main__':
	main()
