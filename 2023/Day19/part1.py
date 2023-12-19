parse_workflows, xmas = list(map(lambda l: l.split('\n'), open("input.txt", "r").read().split('\n\n')))
workflows = {}
for workflow in parse_workflows:
    name, conditions = workflow.replace('}','').split('{')
    eval_str = ''
    for condition in conditions.split(',')[:-1]:
        cond, next = condition.split(':')
        eval_str += '\'' + next + '\'' + ' if ' + cond + ' else '
    eval_str += '\'' + conditions.split(',')[-1] + '\''
    workflows[name] = eval_str
result = 0
for to_eval in xmas:
    vars = []
    vals = []
    to_eval = to_eval[1:-1]
    to_eval = to_eval.split(',')
    for ix, assignment in enumerate(to_eval):
        var, val = assignment.split('=')
        vars.append(var)
        vals.append(val)
    eval_str = ','.join(vars) + ' = ' + ','.join(vals)
    exec(eval_str)
    next = 'in'
    while True:
        next = eval(workflows[next])
        if next == 'A':
            result += x + m + a + s
            break
        if next == 'R':
            break
print(result)
