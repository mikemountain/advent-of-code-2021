def find_difference(shorter, longer):
    for l in shorter:
        longer = longer.replace(l, '')
    return longer

def set_number(bars, numbers):
    for n in numbers:
        if sorted(n) == sorted("".join(set(bars))):
            return n

def in_first_not_second(first, second):
    for l in first:
        if l in second:
            first = first.replace(l, '')
    return first

def is_bar_in_number(bar, number):
    return bar in number

with open('input.txt') as f:
    unique_digits, summed_output = 0, 0
    for line in f:
        # part 1
        right_digits = line.split('|')[1].split()
        for d in right_digits:
            if len(d) in [2, 3, 4, 7]:
                unique_digits += 1
        # part 2
        left_digits = line.split('|')[0].split()

        one = [x for x in left_digits if len(x) == 2][0]
        four = [x for x in left_digits if len(x) == 4][0]
        seven = [x for x in left_digits if len(x) == 3][0]
        eight = [x for x in left_digits if len(x) == 7][0]

        two_three_five = [x for x in left_digits if len(x) == 5]
        zero_six_nine = [x for x in left_digits if len(x) == 6]

        top_bar = find_difference(one, seven)

        # what a mess lmao, there's 100% a better way to do this
        for zsn in zero_six_nine:
            bar = find_difference(four + top_bar, zsn)
            if len(bar) == 1:
                bot_bar = bar
            else:
                p_bot_left = bar
        bot_left = find_difference(bot_bar, p_bot_left)
        nine = set_number(top_bar + bot_bar + four, zero_six_nine)
        zero_six_nine.remove(nine)

        for ttf in two_three_five:
            if len(in_first_not_second(in_first_not_second(eight, ttf), bot_left)) == 2:
                two = ttf
        top_left = in_first_not_second(nine, two + one)
        mid_bar = in_first_not_second(four, one + top_left)
        two_three_five.remove(two)

        for zs in zero_six_nine:
            if mid_bar in zs:
                six = zs
            else:
                zero = zs
        
        for tt in two_three_five:
            if top_left in tt:
                five = tt
            else:
                three = tt

        translation = {"".join(sorted(zero)): '0', "".join(sorted(one)): '1', "".join(sorted(two)): '2', "".join(sorted(three)): '3', "".join(sorted(four)): '4', "".join(sorted(five)): '5', "".join(sorted(six)): '6', "".join(sorted(seven)): '7', "".join(sorted(eight)): '8', "".join(sorted(nine)): '9'}
        right_translated = [translation["".join(sorted(x))] for x in right_digits]
        summed_output += int("".join(right_translated))
        
    print(unique_digits)
    print(summed_output)
