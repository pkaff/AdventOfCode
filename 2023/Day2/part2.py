import math

def get_max_cubes(game):
    rounds = game.split('; ')
    max_cubes = [0 for _ in range(3)]
    for round in rounds:
        cubes = round.split(', ')
        for cube in cubes:
            num, color = cube.split(' ')
            num = int(num)
            if color == 'blue':
                max_cubes[0] = max(max_cubes[0], num)
            if color == 'red':
                max_cubes[1] = max(max_cubes[1], num)
            if color == 'green':
                max_cubes[2] = max(max_cubes[2], num)
    return max_cubes

games = [game.strip().split(': ')[1] for game in open("input.txt", "r").readlines()]
print(sum([math.prod(get_max_cubes(game)) for game in games]))
