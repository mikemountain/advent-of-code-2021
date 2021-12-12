pos, depth, aim = 0, 0, 0

with open('input.txt') as f:
    for line in f:
        direction, amt = line.split()
        if direction == 'forward':
            pos += int(amt)
            depth += int(amt) * aim
            print(depth)
        elif direction == 'down':
            aim += int(amt)
        elif direction == 'up':
            aim -= int(amt)
    print(pos, depth, depth * pos)