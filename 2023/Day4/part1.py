import re
cards = [re.split(':|\|', line.strip())[1:] for line in open("input.txt", "r").readlines()]
cards = [[{int(winner) for winner in winners.split(' ') if str.isdigit(winner)}, {int(bet) for bet in bets.split(' ') if str.isdigit(bet)}] for winners, bets in cards]
print(sum([pow(2, len(winners.intersection(bets)) - 1) for winners, bets in cards if len(winners.intersection(bets)) != 0]))