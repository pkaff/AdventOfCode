MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def is_possible_game(game):
    rounds = game.split('; ')
    for round in rounds:
        cubes = round.split(', ')
        for cube in cubes:
            num, color = cube.split(' ')
            num = int(num)
            if color == 'blue' and num > MAX_BLUE:
                return False
            if color == 'red' and num > MAX_RED:
                return False
            if color == 'green' and num > MAX_GREEN:
                return False
    return True

games = [game.strip().split(': ')[1] for game in open("input.txt", "r").readlines()]
print(sum([ix + 1 for ix, game in enumerate(games) if is_possible_game(game)]))
