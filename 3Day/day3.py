# part 1

# gamma_rate, epsilon_rate = [], []
# bin_array = []
# with open('test_input.txt') as f:
#     for line in f:
#         bin_array.append(line.strip())
#     zipped = tuple(zip(*bin_array))
#     for z in zipped:
#         if z.count('0') > z.count('1'):
#             gamma_rate.append(0)
#             epsilon_rate.append(1)
#         else:
#             gamma_rate.append(1)
#             epsilon_rate.append(0)
#     gr = int(''.join(str(e) for e in gamma_rate), 2)
#     er = int(''.join(str(e) for e in epsilon_rate), 2)
#     print(gr, er, gr * er)

# part 2

bin_array, oxy_array, co2_array = [], [], []
idx = 0
with open('input.txt') as f:
    for line in f:
        bin_array.append(line.strip())
    oxy_array = bin_array.copy()
    co2_array = bin_array.copy()
    while len(oxy_array) > 1:
        zipped = tuple(zip(*oxy_array))
        if zipped[idx].count('0') > zipped[idx].count('1'):
            oxy_array = [x for x in oxy_array if x[idx] == '0']
        else:
            oxy_array = [x for x in oxy_array if x[idx] == '1']
        idx += 1
    idx = 0
    while len(co2_array) > 1:
        zipped = tuple(zip(*co2_array))
        if zipped[idx].count('0') > zipped[idx].count('1'):
            co2_array = [x for x in co2_array if x[idx] == '1']
        else:
            co2_array = [x for x in co2_array if x[idx] == '0']
        idx += 1
    print(int(oxy_array[0], 2) * int(co2_array[0], 2))