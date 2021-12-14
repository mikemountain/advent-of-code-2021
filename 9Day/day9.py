from pprint import pprint

with open('input.txt') as f:
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
            # top left
            if row == 0 and col == 0:
                if spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row + 1][col], initial_grid[row][col + 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # top row
            elif row == 0 and 0 < col < col_size - 1:
                if spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row][col - 1], initial_grid[row + 1][col], initial_grid[row][col + 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # top right
            elif row == 0 and col == col_size - 1:
                if spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row + 1][col], initial_grid[row][col - 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # left col
            elif 0 < row < row_size - 1 and col == 0:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row - 1][col], initial_grid[row + 1][col], initial_grid[row][col + 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # right col
            elif 0 < row < row_size - 1 and col == col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row - 1][col], initial_grid[row + 1][col], initial_grid[row][col - 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # bottom left
            elif row == row_size - 1 and col == 0:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row - 1][col], initial_grid[row][col + 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # bottom row
            elif row == row_size - 1 and 0 < col < col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row - 1][col], initial_grid[row][col - 1], initial_grid[row][col + 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # bottom right
            elif row == row_size - 1 and col == col_size - 1:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row - 1][col], initial_grid[row][col - 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)
            # rest
            else:
                if spot < initial_grid[row - 1][col] and spot < initial_grid[row][col - 1] and spot < initial_grid[row + 1][col] and spot < initial_grid[row][col + 1]:
                    print(spot, 'at', row, col, 'is lower than neighbours:', initial_grid[row + 1][col], initial_grid[row][col + 1], initial_grid[row - 1][col], initial_grid[row][col - 1])
                    print(risk_level, 'increasing by 1 +', spot)
                    risk_level += 1 + spot
                    print(risk_level)

    # pprint(initial_grid)
    print(risk_level)
    