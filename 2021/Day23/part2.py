import sys
from functools import lru_cache
import re
sys.setrecursionlimit(100000)
goal_room_map = {'A':0, 'B':1, 'C': 2, 'D': 3}
rooms = ("BDDB", "ACBC", "ABAD", "DACC", "..#.#.#.#..")
amph_move_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def rreplace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def calculate_room_room_move_cost(start_room, start_room_ix, end_room, end_room_ix, amph):
    nsteps = start_room_ix + 1
    nsteps += abs(start_room - end_room) * 2
    nsteps += end_room_ix + 1
    return amph_move_cost[amph] * nsteps

def calculate_hallway_room_move_cost(room, room_ix, hallway_ix, amph):
    nsteps = abs(2*(room + 1) - hallway_ix)
    nsteps += room_ix + 1
    return amph_move_cost[amph] * nsteps

def hallway_is_blocked(hallway, hallway_ix, top_of_room_hallway_ix):
    if hallway_ix > top_of_room_hallway_ix:
        return len(re.findall(r'[ABCD]', hallway[top_of_room_hallway_ix:hallway_ix])) != 0
    else:
        return len(re.findall(r'[ABCD]', hallway[hallway_ix + 1:top_of_room_hallway_ix])) != 0

def calculate_valid_moves(rooms):
    new_rooms = []
    for room_ix, room in enumerate(rooms[:4]):
        if room != '....':
            start_ix = room.rfind('.')
            start_ix = 0 if start_ix == -1 else start_ix + 1
            amph = room[start_ix]
            goal_room_ix = goal_room_map[amph]
            can_move_to_goal_room = re.match(f'^[{amph}.]+$', rooms[goal_room_ix])
            if room_ix != goal_room_ix and can_move_to_goal_room and not hallway_is_blocked(rooms[4], (goal_room_ix + 1)*2, (room_ix + 1) * 2):
                end_ix = rooms[goal_room_ix].rfind('.')
                updated_end_room = rreplace(rooms[goal_room_ix], '.', amph)
                updated_start_room = room.replace(amph, '.', 1)
                new_room_tpl = None
                if goal_room_ix > room_ix:
                    new_room_tpl = rooms[0:room_ix] + (updated_start_room,) + rooms[room_ix + 1:goal_room_ix] + (updated_end_room,) + rooms[goal_room_ix + 1:]
                else:
                    new_room_tpl = rooms[0:goal_room_ix] + (updated_end_room,) + rooms[goal_room_ix + 1:room_ix] + (updated_start_room,) + rooms[room_ix + 1:]
                new_rooms.append((new_room_tpl, calculate_room_room_move_cost(room_ix, start_ix, goal_room_ix, end_ix, amph)))
            for hallway_ix, spot in [(ix, spot) for ix, spot in enumerate(rooms[4]) if spot == '.']:
                top_of_room_hallway_ix = (room_ix + 1) * 2
                hallway_blocked = hallway_is_blocked(rooms[4], hallway_ix, top_of_room_hallway_ix)
                wants_to_move = room_ix != goal_room_ix or not can_move_to_goal_room
                if not hallway_blocked and wants_to_move:
                    updated_start_room = room.replace(amph, '.', 1)
                    updated_hallway = rooms[4][:hallway_ix] + amph + rooms[4][hallway_ix + 1:]
                    new_room_tpl = rooms[:room_ix] + (updated_start_room,) + rooms[room_ix + 1:-1] + (updated_hallway,)
                    new_rooms.append((new_room_tpl, calculate_hallway_room_move_cost(room_ix, start_ix, hallway_ix, amph)))
    for hallway_ix, amph in [(ix, amph) for ix, amph in enumerate(rooms[4]) if amph not in ['.', '#']]:
        goal_room_ix = goal_room_map[amph]
        top_of_room_hallway_ix = (goal_room_ix + 1) * 2
        hallway_blocked = hallway_is_blocked(rooms[4], hallway_ix, top_of_room_hallway_ix)
        if re.match(f'^[{amph}.]+$', rooms[goal_room_ix]) and not hallway_blocked:
            end_ix = rooms[goal_room_ix].rfind('.')
            updated_end_room = rreplace(rooms[goal_room_ix], '.', amph)
            updated_hallway = rooms[4][:hallway_ix] + '.' + rooms[4][hallway_ix + 1:]
            new_room_tpl = rooms[0:goal_room_ix] + (updated_end_room,) + rooms[goal_room_ix + 1:-1] + (updated_hallway,)
            new_rooms.append((new_room_tpl, calculate_hallway_room_move_cost(goal_room_ix, end_ix, hallway_ix, amph)))
    return new_rooms

@lru_cache(maxsize=None)
def recursive_move(rooms):
    if all([c == 'A' for c in rooms[0]]) and all([c == 'B' for c in rooms[1]]) and all([c == 'C' for c in rooms[2]]) and all([c == 'D' for c in rooms[3]]):
        return 0

    valid_moves = calculate_valid_moves(rooms)
    best_score = sys.maxsize
    for new_rooms, score_to_move in valid_moves:
        total_score = score_to_move + recursive_move(new_rooms)
        best_score = min(best_score, total_score)
    return best_score

print(recursive_move(rooms))


