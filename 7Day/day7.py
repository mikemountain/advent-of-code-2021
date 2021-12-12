import statistics

with open('input.txt') as f:
    line = f.readline().split(',')
    positions = [int(i) for i in line]
    part_1_fuel, part_2_fuel = 0, -1
    median = statistics.median(positions)
    min_position = min(positions)
    max_position = max(positions)
    for p in positions:
        part_1_fuel += abs(p - median)
    for r in range(min_position, max_position):
        temp_fuel = 0
        for p in positions:
            n = abs(p - r)
            temp_fuel += (n**2 + n) / 2
        if temp_fuel < part_2_fuel or part_2_fuel == -1:
            print('choosing ', r, 'fuel ', temp_fuel)
            part_2_fuel = temp_fuel
    print('part 1:', int(part_1_fuel))
    print('part 2:', int(part_2_fuel))
