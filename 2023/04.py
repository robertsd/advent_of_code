with open("04.txt") as f:
    data = f.read().splitlines()


def score(card):
    (winners, numbers) = card.split(':')[1].split('|')
    match_count = sum([1 if n.isnumeric() and n in winners.strip().split(' ') else 0 for n in numbers.strip().split(' ')])
    return 2**(match_count - 1) if match_count > 0 else 0


def revised_score(card):
    (winners, numbers) = card.split(':')[1].split('|')
    match_count = sum([1 if n.isnumeric() and n in winners.strip().split(' ') else 0 for n in numbers.strip().split(' ')])
    return match_count 


def won(card_id, data):
    cards_won = data[card_id : card_id + revised_score(data[card_id-1])]
    win_ids = [int(card.split(':')[0].split(' ')[-1]) for card in cards_won]
    return len(cards_won) + sum([won(win_id, data) for win_id in win_ids]) if revised_score(data[card_id-1]) > 0 else 0


print("Part 1:", sum([score(card) for card in data]))
print("Part 2:", sum([won(i, data) for i in range(1, len(data)+1)]) + len(data))
