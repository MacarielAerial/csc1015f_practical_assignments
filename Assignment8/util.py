# utility module function
def create_grid(grid):
	"""create a 4x4 array of zeroes within grid"""
	for row in range(4):
		grid.append([])
		for column in range(4):
			grid[row].append(0)
	return grid

def print_grid(grid):
	"""print out a 4x4 grid in 5-width columns within a box"""
	print('+--------------------+')
	for row in range(len(grid)):
		print('|', end="")
		for column in range(len(grid[row])):
			if grid[row][column] == 0:
				print('     ', end="")
			else:
				print(grid[row][column], ' '*(5-len(str(grid[row][column]))), sep="", end="")
		print('|')
	print('+--------------------+')

def check_lost(grid):
	"""return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
	judgement = True
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			if grid[row][column] == 0:
				judgement = False
			elif row == 0:
				if grid[row][column] == grid[row+1][column]:
					judgement = False
			elif row == 1 or row == 2:
				if grid[row][column] == grid[row-1][column]:
					judgement = False
				if grid[row][column] == grid[row+1][column]:
					judgement = False
			elif row == 3:
				if grid[row][column] == grid[row-1][column]:
					judgement = False
			elif column == 0:
				if grid[row][column] == grid[row][column+1]:
					judgement = False
			elif column == 3:
				if grid[row][column] == grid[row][column-1]:
					judgement = False
			elif column == 1 or column == 2:
				if grid[row][column] == grid[row][column+1]:
					judgement = False
				if grid[row][column] == grid[row][column-1]:
					jugement = False
	return judgement

def check_won(grid):
	"""return True if a value>=32 is found in the grid; otherwise false"""
	judgement = False
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			if grid[row][column] >= 32:
				judgement = True
	return judgement

def copy_grid(grid):
	"""return a copy of the given grid"""
	copy_grid = []
	for row in range(len(grid)):
		copy_grid.append([])
		for column in range(len(grid[row])):
			copy_grid[row].append(grid[row][column])
	return copy_grid

def grid_equal(grid1, grid2):
	"""check if 2 grids are equal - return boolean value"""
	judgement = True
	for row in range(len(grid2)):
		for column in range(len(grid2)):
			if grid2[row][column] != grid1[row][column]:
				judgement = False
	return judgement



if __name__ == "__main__":
	grid1 = [[32,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	grid2 = [[33,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	print(grid_equal(grid1,grid2))
