from pprint import pprint

def update_cards(bingo_cards, number):
    for card in bingo_cards:
        for i, row in enumerate(card):
            new_row = [x if x != number else 'X' for x in row]
            card[i] = new_row
        # pprint(card)

def check_cards(bingo_cards, num):
    for card in bingo_cards:
        row_winner = True
        col_winner = True
        for row in card:
            row_winner = all(x == 'X' for x in row)
            if row_winner:
                print("we won!")
                break
        if not row_winner:
            zipped = tuple(zip(*card))
            for z in zipped:
                col_winner = all(x == 'X' for x in z)
                if col_winner:
                    break
        if row_winner or col_winner:
            score = 0
            for row in card:
                score += sum(filter(lambda i: isinstance(i, int), row))
            score *= num
            print(score)
            break
    return row_winner or col_winner

def check_last_card(bingo_cards, num):
    for card in bingo_cards:
        row_winner = True
        col_winner = True
        for row in card:
            row_winner = all(x == 'X' for x in row)
            if row_winner:
                break
        if not row_winner:
            zipped = tuple(zip(*card))
            for z in zipped:
                col_winner = all(x == 'X' for x in z)
                if col_winner:
                    break
        if row_winner or col_winner:
            print('removing card because of number:', num)
            pprint(card)
            bingo_cards.remove(card)
            if len(bingo_cards) == 0:
                print(num)
                pprint(card)
                score = 0
                for row in card:
                    score += sum(filter(lambda i: isinstance(i, int), row))
                score *= num
                print(score)
                return []
    return bingo_cards

def main():
    bingo_cards = []
    with open('input.txt') as f:
        numbers_to_call = f.readline().split(',')
        numbers_to_call = [int(i) for i in numbers_to_call]
        _ = f.readline()
        card = []
        for line in f:
            if line == "\n":
                bingo_cards.append(card)
                card = []
            else:
                row = [int(i) for i in line.split()]
                card.append(row)
    for num in numbers_to_call:
        update_cards(bingo_cards, num)
        bingo_cards = check_last_card(bingo_cards, num)
        if len(bingo_cards) == 0:
            break

if __name__ == "__main__":
    main()