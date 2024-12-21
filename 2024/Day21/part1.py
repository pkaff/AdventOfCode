from functools import lru_cache
input = [line.strip() for line in open("input.txt", "r").readlines()]
num_pad = ['789', '456', '123', '#0A']
num_pad_positions = {c : (x, y) for y, row in enumerate(num_pad) for x, c in enumerate(row)}
dir_pad = ['#^A', '<v>']
dir_pad_positions = {c : (x, y) for y, row in enumerate(dir_pad) for x, c in enumerate(row)}

def get_dirs(from_pos, to_pos, invalid_pos):
    dx = to_pos[0] - from_pos[0]
    dy = to_pos[1] - from_pos[1]
    x_dir = '<' if dx < 0 else '>'
    y_dir = '^' if dy < 0 else 'v'
    if dx == 0 and dy == 0:
        yield 'A'
    elif dy == 0:
        yield x_dir * abs(dx) + 'A'
    elif dx == 0:
        yield y_dir * abs(dy) + 'A'
    else:
        if not (
            (invalid_pos[0] == to_pos[0] and invalid_pos[1] in abs_range(from_pos[1], to_pos[1]))
            or (invalid_pos[1] == from_pos[1] and invalid_pos[0] in abs_range(to_pos[0], from_pos[0]))
        ):
            yield x_dir * abs(dx) + y_dir * abs(dy) + 'A'
        if not (
            (invalid_pos[0] == from_pos[0] and invalid_pos[1] in abs_range(to_pos[1], from_pos[1]))
            or (invalid_pos[1] == to_pos[1] and invalid_pos[0] in abs_range(from_pos[0], to_pos[0]))
        ):
            yield y_dir * abs(dy) + x_dir * abs(dx) + 'A'

def abs_range(start, stop):
    if start < stop:
        return range(start, stop)
    else:
        return range(start, stop, -1)

@lru_cache(maxsize=None)
def find_shortest_sequence(code, level, is_numpad):
    sequences = get_possible_sequences(code, is_numpad, 'A')
    if level == 0:
        return min(sum(len(part) for part in sequence) for sequence in sequences)
    else:
        return min(sum(find_shortest_sequence(dirpad_code, level - 1, is_numpad=False) for dirpad_code in sequence) for sequence in sequences)

def get_possible_sequences(code, is_numpad, from_char):
    if code == '':
        return [[]]
    keypad_pos = num_pad_positions if is_numpad else dir_pad_positions
    from_pos = keypad_pos[from_char]
    to_pos = keypad_pos[code[0]]
    invalid_pos = keypad_pos['#']

    return [[dirs, *sequence] for sequence in get_possible_sequences(code[1:], is_numpad, code[0]) for dirs in get_dirs(from_pos, to_pos, invalid_pos)]

print(sum(int(code[:-1]) * find_shortest_sequence(code, 2, True) for code in input))