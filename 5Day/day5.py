from pprint import pprint

# initial_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(10)]
initial_grid = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    initial_grid.append(row)

with open('input.txt') as f:
    # I don't know why my coordinates are backwards but oh well?
    for l in f:
        row = l.split()
        x1, y1 = row[0].split(',')
        x2, y2 = row[-1].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 == x2:
            if y1 < y2:
                for y in range(y1, y2+1):
                    initial_grid[y][x1] += 1
            else:
                for y in range(y1, y2-1, -1):
                    initial_grid[y][x1] += 1

        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2+1):
                    initial_grid[y1][x] += 1
            else:
                for x in range(x1, x2-1, -1):
                    initial_grid[y1][x] += 1

        else:
            if y1 < y2 and x1 < x2:
                initial_grid[y1][x1] += 1
                while y1 != y2 and x1 != x2:
                    y1 += 1
                    x1 += 1
                    initial_grid[y1][x1] += 1

            elif y1 < y2 and x1 > x2:
                initial_grid[y1][x1] += 1
                while y1 != y2 and x1 != x2:
                    y1 += 1
                    x1 -= 1
                    initial_grid[y1][x1] += 1
                    
            elif y1 > y2 and x1 < x2:
                initial_grid[y1][x1] += 1
                while y1 != y2 and x1 != x2:
                    y1 -= 1
                    x1 += 1
                    initial_grid[y1][x1] += 1

            elif y1 > y2 and x1 > x2:
                initial_grid[y1][x1] += 1
                while y1 != y2 and x1 != x2:
                    y1 -= 1
                    x1 -= 1
                    initial_grid[y1][x1] += 1

    overlaps = 0
    for row in initial_grid:
        overlaps += len([x for x in row if x > 1])
    print(overlaps)
    # pprint(initial_grid)