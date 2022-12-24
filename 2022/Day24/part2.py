from collections import deque
grid = [[c for c in line.strip('\n')] for line in open("input.txt", "r").readlines()]
boundaryMaxCol = len(grid[0]) - 1
maxCol = boundaryMaxCol - 1
boundaryMaxRow = len(grid) - 1
maxRow = boundaryMaxRow - 1
start = (0, 1)
stop = (boundaryMaxRow, boundaryMaxCol - 1)

def is_boundary(pos):
    return pos != start and pos != stop and (pos[0] == 0 or pos[0] == boundaryMaxRow or pos[1] == 0 or pos[1] == boundaryMaxCol)

def is_in_bounds(pos):
    return pos == start or pos == stop or (pos[0] >= 0 and pos[0] <= boundaryMaxRow and pos[1] >= 0 and pos[1] <= boundaryMaxCol)

def print_grid(pos, up_tornados, down_tornados, left_tornados, right_tornados, time):
    printstr = ''
    for row in range(boundaryMaxRow + 1):
        for col in range(boundaryMaxCol + 1):
            if is_boundary((row, col)):
                printstr += '#'
            elif (row, col) == pos:
                printstr += 'E'
            else:
                tornados_at_pos = [((row + time - 1) % maxRow + 1, col) in up_tornados, ((row - time - 1) % maxRow + 1, col) in down_tornados, (row, (col + time - 1) % maxCol + 1) in left_tornados, (row, (col - time - 1) % maxCol + 1) in right_tornados]
                n_tornados = sum(tornados_at_pos)
                if n_tornados == 0:
                    printstr += '.'
                elif n_tornados != 1:
                    printstr += str(sum(tornados_at_pos))
                else:
                    if tornados_at_pos[0]:
                        printstr += '^'
                    if tornados_at_pos[1]:
                        printstr += 'v'
                    if tornados_at_pos[2]:
                        printstr += '<'
                    if tornados_at_pos[3]:
                        printstr += '>'
        printstr += '\n'
    print(printstr)

def tornados_blocking(pos, up_tornados, down_tornados, left_tornados, right_tornados, time):
    up_blocking = ((pos[0] + time - 1) % maxRow + 1, pos[1]) in up_tornados
    down_blocking = ((pos[0] - time - 1) % maxRow + 1, pos[1]) in down_tornados
    left_blocking = (pos[0], (pos[1] + time - 1) % maxCol + 1) in left_tornados
    right_blocking = (pos[0], (pos[1] - time - 1) % maxCol + 1) in right_tornados
    return any([up_blocking, down_blocking, left_blocking, right_blocking])

def get_next_possible_moves(cur_pos, target, up_tornados, down_tornados, left_tornados, right_tornados, time):
    potential_moves = [(cur_pos[0] + 1, cur_pos[1]), (cur_pos[0] - 1, cur_pos[1]), (cur_pos[0], cur_pos[1] + 1), (cur_pos[0], cur_pos[1] - 1), (cur_pos[0], cur_pos[1])]
    return [next_pos for next_pos in potential_moves if next_pos == target or (not is_boundary(next_pos) and is_in_bounds(next_pos) and not tornados_blocking(next_pos, up_tornados, down_tornados, left_tornados, right_tornados, time))]

up_tornados = {(row, col) for row, line in enumerate(grid) for col, dir in enumerate(line) if dir == '^'}
down_tornados = {(row, col) for row, line in enumerate(grid) for col, dir in enumerate(line) if dir == 'v'}
left_tornados = {(row, col) for row, line in enumerate(grid) for col, dir in enumerate(line) if dir == '<'}
right_tornados = {(row, col) for row, line in enumerate(grid) for col, dir in enumerate(line) if dir == '>'}
print_grid(start, up_tornados, down_tornados, left_tornados, right_tornados, 0)

def bfs(start, stop, start_time):
    frontier = deque()
    frontier.append((start_time, start))
    visited = set((start, start_time))
    while frontier:
        time, pos = frontier.popleft()
        if (pos, time) in visited:
            continue
        visited.add((pos, time))
        if pos == stop:
            return time
        #print("Minute ", time)
        #print_grid(pos, up_tornados, down_tornados, left_tornados, right_tornados, time)

        next_moves = get_next_possible_moves(pos, stop, up_tornados, down_tornados, left_tornados, right_tornados, time + 1)
        for move in next_moves:
            frontier.append((time + 1, move))

time = bfs(start, stop, 0)
time2 = bfs(stop, start, time)
time3 = bfs(start, stop, time2)
print(time3)