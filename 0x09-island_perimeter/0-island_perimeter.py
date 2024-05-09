def island_perimeter(grid):
    perimeter = 0
    
    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Check if the current cell is land
                perimeter += 4  # Increment perimeter for each land cell
                
                # Check neighboring cells (top, bottom, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if top neighbor is land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if left neighbor is land
    
    return perimeter