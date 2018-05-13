# a routine module for 2048 program

def push_up(grid):
	"""merge grid values upwards"""
# Eliminate all the gaps --> zero values in except in last row
	while 0 in grid[0]:
		for row in range(len(grid)):
			for column in range(len(grid[row])):
				if row == 0:
					if grid[row][column] == 0:
						grid[row][column] = grid[row+1][column]
						grid[row+1][column] = grid[row+2][column]
						grid[row+2][column] = grid[row+3][column]
						grid[row+3][column] = 0
				if row == 1:
					if grid[row][column] == 0:
						grid[row][column] = grid[row+1][column]
						grid[row+1][column] = grid[row+2][column]
						grid[row+2][column] = 0
				if row == 2:
					if grid[row][column] == 0:
						grid[row][column] = grid[row+1][column]
						grid[row+1][column] = 0
				if grid[0][column] == 0 and grid[1][column] == 0 and grid[2][column] ==0 and grid[3][column] == 0:
					break
# Perform summation in values adjacent and equavalent to each other
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			if row == 0:
				if grid[row][column] == grid[row+1][column]:
					grid[row][column] += grid[row+1][column]
					grid[row+1][column] = grid[row+2][column]
					grid[row+2][column] = grid[row+3][column]
					grid[row+3][column] = 0
			if row == 1:
				if grid[row][column] == grid[row+1][column]:
					grid[row][column] += grid[row+1][column]
					grid[row+1][column] = grid[row+2][column]
					grid[row+2][column] = 0
			if row == 2:
				if grid[row][column] == grid[row+1][column]:
					grid[row][column] += grid[row+1][column]
					grid[row+1][column] = 0

def push_down(grid):
	"""merge grid values downwards"""
	while 0 in grid[3]:
		for row in range(len(grid)-1, -1, -1):
			for column in range(len(grid[row])):
				if row == 3:
					if grid[row][column] == 0:
						grid[row][column] = grid[row-1][column]
						grid[row-1][column] = grid[row-2][column]
						grid[row-2][column] = grid[row-3][column]
						grid[row-3][column] = 0
				if row == 2:
					if grid[row][column] == 0:
						grid[row][column] = grid[row-1][column]
						grid[row-1][column] = grid[row-2][column]
						grid[row-2][column] = 0
				if row == 1:
					if grid[row][column] == 0:
						grid[row][column] = grid[row-1][column]
						grid[row-1][column] = 0
				if grid[0][column] == 0 and grid[1][column] == 0 and grid[2][column] == 0 and grid[3][column] == 0:
					break
	for row in range(len(grid)-1, -1, -1):
		for column in range(len(grid[row])):
			if row == 3:
				if grid[row][column] == grid[row-1][column]:
					grid[row][column] += grid[row-1][column]
					grid[row-1][column] = grid[row-2][column]
					grid[row-2][column] = grid[row-3][column]
					grid[row-3][column] = 0
			if row == 2:
				if grid[row][column] == grid[row-1][column]:
					grid[row][column] += grid[row-1][column]
					grid[row-1][column] = grid[row-2][column]
					grid[row-2][column] = 0
			if row == 1:
				if grid[row][column] == grid[row-1][column]:
					grid[row][column] += grid[row-1][column]
					grid[row-1][column] = 0












if __name__ == "__main__":
	grid = [[0,2,2,4], [0,0,4,0], [4,8,0,2],[4,2,0,2]]
	for item in grid:
		print(item, end="\n")
	push_down(grid)
	print("\n"*4)
	for item in grid:
		print(item, end="\n")
	#push_down(grid)
	#print("\n"*4)
	#for item in grid:
		#print(item, end="\n")
