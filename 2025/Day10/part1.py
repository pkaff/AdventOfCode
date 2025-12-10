from ast import literal_eval

input = [line.strip().split() for line in open("input.txt", "r").readlines()]
def count_presses(target, buttons):
    to_visit = [(button, 1, '.'*len(target)) for button in buttons]
    visited = set()
    visited.add('.'*len(target))
    while to_visit:
        button, num_presses, cur = to_visit.pop(0)
        new_cur = list(cur)
        for strix in button:
            new_cur[strix] = '.' if new_cur[strix] != '.' else '#'
        new_cur_str = ''.join(new_cur)
        if new_cur_str in visited:
            continue
        visited.add(new_cur_str)
        if new_cur_str == target:
            return num_presses
        for next_button in buttons:
            to_visit.append((next_button, num_presses + 1, new_cur_str))

presses = 0
for row in input:
    goal = row[0][1:-1]
    buttons = tuple(literal_eval(t) if len(t) > 3 else (literal_eval(t),) for t in row[1:-1])
    presses += count_presses(goal, buttons)
print(presses)
