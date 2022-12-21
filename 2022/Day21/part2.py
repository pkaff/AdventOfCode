input = {line.split(':')[0]: line.strip('\n').split(': ')[1] for line in open("input.txt", "r").readlines()}
input['root'] = input['root'].replace('+', '==')
input['humn'] = '1j'
def dfs(key):
    val = input[key]
    if key == 'humn':
        return f'{val}'
    if val.isdigit():
        return f'{val}'

    left, op, right = val.split()

    left_eval = dfs(left)
    right_eval = dfs(right)
    return f'{eval(left_eval)}{op}{eval(right_eval)}'
eval_str = dfs("root")
print(eval_str)