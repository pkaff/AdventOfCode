from collections import namedtuple
Player = namedtuple('Player', 'pos score')
space_scores = [i for i in range(1, 10 + 1)]
players = [Player(0, 0), Player(9, 0)] #positions offset by -1, so pos 0-9 has score 1-10
n_rolls = [0]
def roller_gen(n_rolls):
    roll = 1
    while True:
        n_rolls[0] += 1
        yield roll
        roll = (roll + 1) % 100
        if roll == 0:
            roll = 100
roller = roller_gen(n_rolls)
turn = 0
while all([player.score < 1000 for player in players]):
    steps = sum([next(roller) for _ in range(3)])
    new_pos = (players[turn].pos + steps) % 10
    new_score = players[turn].score + space_scores[new_pos]
    players[turn] = Player(new_pos, new_score)
    turn = (turn + 1) % 2
print(n_rolls[0] * min(players, key=lambda player: player.score).score)
