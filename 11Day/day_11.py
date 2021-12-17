from pprint import pprint

grid = []
fl = 0

def flash(flash_coords):
    flashes = 0
    row_size = len(grid)
    col_size = len(grid[0])
    for row, col in flash_coords:
        flashes += 1
        grid[row][col] = 0
        for r, c in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            rr, cc = row + r, col + c
            if 0 <= rr < row_size and 0 <= cc < col_size:
                if 0 < grid[rr][cc]:
                    grid[rr][cc] += 1
    return flashes

def check_flash(flash_coords):
    flashes_done = True
    synchronised = True
    row_size = len(grid)
    for row in range(row_size):
        col_size = len(grid[row])
        for col in range(col_size):
            if grid[row][col] > 0:
                synchronised = False
            if grid[row][col] > 9:
                flashes_done = False
                flash_coords.append([row, col])
    return flashes_done, synchronised, flash_coords

def run_step():
    row_size = len(grid)
    for row in range(row_size):
        col_size = len(grid[row])
        for col in range(col_size):
            grid[row][col] += 1

with open('input.txt') as f:
    for line in f:
        row = []
        for c in line.strip():
            row.append(int(c))
        grid.append(row)

fl = 0
step = 0

while True:
    run_step()
    step += 1
    flash_coords = []
    while True:
        flashes_done, synchronised, flash_coords = check_flash([])
        if flashes_done:
            break
        fl += flash(flash_coords)
    if synchronised:
        print(step)
        break
    if step == 100:
        print(fl)

