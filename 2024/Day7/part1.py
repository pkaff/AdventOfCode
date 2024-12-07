input = [(int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split()))) for line in open("input.txt", "r").readlines()]
def greedy_search(target, cur_res, to_eval):
    if len(to_eval) == 0:
        return cur_res == target
    if cur_res > target:
        return False
    return greedy_search(target, cur_res * to_eval[0], to_eval[1:]) or greedy_search(target, cur_res + to_eval[0], to_eval[1:])

print(sum([target if greedy_search(target, equation[0], equation[1:]) else 0 for target, equation in input]))