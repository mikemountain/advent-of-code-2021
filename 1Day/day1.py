from collections import deque

current_depth, single_measurements, summed_measurements = 0, 0, 0
current_depths = deque(maxlen = 3)
new_depths = deque(maxlen = 3)

f = open("input.txt", "r")
# part 1

# for line in f:
#     if int(line) > current_depth and current_depth != 0:
#         single_measurements += 1
#     current_depth = int(line)

# part 2
for l in f:
    depth = int(l)
    if len(current_depths) < 3:
        new_depths.append(depth)
        current_depths.append(depth)
        continue

    current_depths = new_depths.copy()
    new_depths.append(depth)
    if sum(new_depths) > sum(current_depths):
        summed_measurements += 1

print(single_measurements)
print(summed_measurements)