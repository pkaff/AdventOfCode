input = {line.split(':')[0]: line.strip('\n').split(': ')[1] for line in open("testinput.txt", "r").readlines()}
input['root'] = input['root'].replace('+', '==')
input['humn'] = 'humn + 0'
print(input)
def get_humn_simplified_num(eval_str):
    if eval_str == 'humn':
        return ''
    eval_str = eval_str.replace('humn', '1')
    return f'{eval(eval_str)}'
def get_humn_op(eval_str, op):
    if eval_str == 'humn':
        return op
    if '*' in eval_str:
        return '*'
    elif '/' in eval_str:
        return '/'
def simplify(left_str, op, right_str):
    if op == '+' or op == '-':
        if 'humn' in left_str:
            humn_eval, _, human_add  = left_str.split()
            return f'{humn_eval} + {eval(f"{human_add}{op}{right_str}")}'
        if 'humn' in right_str:
            humn_eval, _, human_add  = right_str.split()
            return f'{humn_eval} + {eval(f"{human_add}{op}{left_str}")}'
    elif op == '*' or op == '/':
        if 'humn' in left_str:
            humn_eval, _, human_add  = left_str.split()
            simplified_num = get_humn_simplified_num(f'({humn_eval}){op}{right_str}')
            humn_op = get_humn_op(humn_eval, op)
            return f'{simplified_num}{humn_op}humn + {eval(f"{human_add}{op}{right_str}")}'
        if 'humn' in right_str:
            humn_eval, _, human_add  = right_str.split()
            simplified_num = get_humn_simplified_num(f'{left_str}{op}({humn_eval})')
            humn_op = get_humn_op(humn_eval, op)
            return f'{simplified_num}{humn_op}humn + {eval(f"{left_str}{op}{human_add}")}'
    elif op == '==':
        return f'{left_str}{op}{right_str}'
    assert(False)
def dfs(key):
    val = input[key]
    if key == 'humn':
        return f'{val}'
    if val.isdigit():
        return f'{val}'

    left, op, right = val.split()

    left_eval = dfs(left)
    right_eval = dfs(right)
    if 'humn' not in left_eval and 'humn' not in right_eval:
        return f'{eval(left_eval + op + right_eval)}'

    return simplify(left_eval, op, right_eval)

humn = 0
print(dfs("root"))
# print(eval_str)
# lhs, rhs = eval_str.split(' + ')
# print(lhs, rhs)
# rhs = f"{eval(rhs.replace('==', '+').replace('-', '+'))}"
# print(rhs)
# first_eval = eval(lhs[:lhs.index('*humn/')])
# print(first_eval)
# second_eval = eval(lhs[lhs.index('*humn/') + 6:])
# print(second_eval)
# print(eval(f"{rhs}*{second_eval}/{first_eval}"))
