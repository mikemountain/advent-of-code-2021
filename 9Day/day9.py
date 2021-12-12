from pprint import pprint

with open('test_input.txt') as f:
    initial_grid = []
    for line in f:
        l = list(line.split(',')[0].strip())
        initial_grid.append([int(x) for x in l])
    pprint(initial_grid)
    risk_level = 0
    for i in range(max(0, po))
    # row_limit = len(initial_grid) - 1
    # col_limit = len(initial_grid[0]) - 1
    # print(row_limit, col_limit)
    # for row in initial_grid:
    #     for col in row:
    #         spot = initial_grid[row][col]

            # if row != 0 and col != 0 and row != len(initial_grid) and col != len(row):
            #     if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot
            # elif row != 0 and col == 0 and row != len(initial_grid):
            #     if spot < initial_grid[row - 1][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot
            # elif row == 0 and col != 0 and col != len(row):
            #     if spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot
            # elif row == 0 and col == 0:
            #     if spot < initial_grid[row][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot
            # elif row == len(initial_grid) and col == 0:
            #     if spot < initial_grid[row][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot
            # elif row == 0 and col == 0:
            #     if spot < initial_grid[row][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
            #         risk_level += 1 + spot