import re
cards = [re.split(':|\|', line.strip())[1:] for line in open("input.txt", "r").readlines()]
cards = [[{int(winner) for winner in winners.split(' ') if str.isdigit(winner)}, {int(bet) for bet in bets.split(' ') if str.isdigit(bet)}] for winners, bets in cards]
n_cards = [1] * len(cards)
for ix, (winners, bets) in enumerate(cards):
    n_wins = len(winners.intersection(bets))
    for increase_ix in range(ix + 1, ix + 1 + n_wins):
        n_cards[increase_ix] += n_cards[ix]
print(sum(n_cards))