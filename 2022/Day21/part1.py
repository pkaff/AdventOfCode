input = {line.split(':')[0]: line.strip('\n').split(': ')[1] for line in open("input.txt", "r").readlines()}

def dfs(key):
    val = input[key]
    if val.isdigit():
        return f'{val}'

    left, op, right = val.split()

    return f"{eval(dfs(left) + op + dfs(right))}"

print(int(dfs('root')))