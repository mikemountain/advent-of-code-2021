characters = {'{':'}', '[':']', '<':'>', '(':')'}
boint_map = {'}': 1197, ']': 57, '>': 25137, ')': 3}
part_2_boint_map = {'}': 3, ']': 2, '>': 4, ')': 1}
boints = 0
scores = []

with open('input.txt') as f:
    for line in f:
        complete, trace = [], []
        need = ''
        l = list(line.strip())
        list_len = len(l) - 1
        pos = -1
        part_2_boints = 0
        for c in l:
            pos += 1
            if c in characters.keys():
                trace.append(c)
                need = characters[c]
            elif c == need:
                trace.pop()
                if len(trace) > 0:
                    need = characters[trace[-1]]
            else:
                boints += boint_map[c]
                break
            if pos == list_len and len(trace) > 0:
                trace.reverse()
                for crap in trace:
                    part_2_boints *= 5
                    part_2_boints += part_2_boint_map[characters[crap]]
                scores.append(part_2_boints)

    scores.sort()
    mid = int((len(scores) - 1) / 2)
    print(boints)
    print(scores[mid])