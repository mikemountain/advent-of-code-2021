from pprint import pprint

def explore(grid, row, col, max_row, max_col, basin_coords):
    for r, c in [[-1,0], [1,0], [0,-1], [0,1]]:
        rr, cc = row + r, col + c
        if 0 <= rr < max_row and 0 <= cc < max_col and not [rr, cc] in basin_coords:
            if grid[rr][cc] < 9:
                basin_coords.append([rr, cc])
                basin_coords = explore(grid, rr, cc, max_row, max_col, basin_coords)
    return basin_coords

with open('input.txt') as f:
    basins = []
    pools = 1
    basin_coords = []
    initial_grid = []
    for line in f:
        l = list(line.split(',')[0].strip())
        initial_grid.append([int(x) for x in l])
    risk_level = 0
    row_size = len(initial_grid)
    for row in range(row_size):
        col_size = len(initial_grid[row])
        for col in range(col_size):
            spot = initial_grid[row][col]
            if not spot == 9:
                basin_coords = explore(initial_grid, row, col, row_size, col_size, basin_coords)
                basin_coords.sort()
                if not basin_coords in basins:
                    basins.append(basin_coords)
            basin_coords = []
            # top left
            if row == 0 and col == 0:
                if spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot

            # top row
            elif row == 0 and 0 < col < col_size - 1:
                if spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot

            # top right
            elif row == 0 and col == col_size - 1:
                if spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col]:
                    risk_level += 1 + spot

            # left col
            elif 0 < row < row_size - 1 and col == 0:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot

            # right col
            elif 0 < row < row_size - 1 and col == col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col]:
                    risk_level += 1 + spot

            # bottom left
            elif row == row_size - 1 and col == 0:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot

            # bottom row
            elif row == row_size - 1 and 0 < col < col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot

            # bottom right
            elif row == row_size - 1 and col == col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1]:
                    risk_level += 1 + spot

            # rest
            else:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    risk_level += 1 + spot
    
    basins.sort(reverse = True, key = len)
    for b in basins[:3]:
        pools *= len(b)

    # pprint(initial_grid)
    print(risk_level)
    print(pools)
