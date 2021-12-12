from collections import deque

fish_deq = deque(maxlen = 9)

with open('input.txt') as f:
    line = f.readline().split(',')
    initial_state = [int(i) for i in line]
    initial_state.sort()
    for i in range(9):
        fish_deq.append(initial_state.count(i))
    for day in range(256):
        babies = fish_deq.popleft()
        fish_deq.append(babies)
        fish_deq[6] += babies
    print(sum(fish_deq))

    # lmao first attempt, bad
    # for day in range(80):
    #     append = 0
    #     for i, t in enumerate(initial_state):
    #         initial_state[i] -= 1
    #         if t == 0:
    #             append += 1
    #             initial_state[i] = 6
    #     for x in range(append):
    #         initial_state.append(8)
    #     print('day:', day, len(initial_state))
    