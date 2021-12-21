from functools import lru_cache
from collections import namedtuple
Player = namedtuple('Player', 'pos score')
space_scores = [i for i in range(1, 10 + 1)]
players = (Player(0, 0), Player(9, 0)) #positions offset by -1, so pos 0-9 has score 1-10

@lru_cache(maxsize=None)
def recursive_play(players, turn, rolls):
    if len(rolls) == 3:
        new_pos = (players[turn].pos + sum(rolls)) % 10
        new_score = players[turn].score + space_scores[new_pos]
        players = tuple(Player(new_pos, new_score) if ix == turn else players[ix] for ix in range(2))
        if new_score >= 21:
            return [1 if ix == turn else 0 for ix in range(2)]
        turn = (turn + 1) % 2
        rolls = tuple()
    n_wins = [0, 0]
    for roll in range(1, 3 + 1):
        n_sub_wins = recursive_play(players, turn, rolls + (roll,))
        n_wins[0] += n_sub_wins[0]
        n_wins[1] += n_sub_wins[1]
    return n_wins

print(max(recursive_play(players, 0, ())))
