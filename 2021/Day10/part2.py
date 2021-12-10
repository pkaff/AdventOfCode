from statistics import median
myin = [line.replace('\n', '') for line in open("input.txt", "r").readlines()]
open_tokens = '[({<'
close_tokens = '])}>'
token_score_map = {'(': 1, '[': 2, '{': 3, '<': 4}
autocomplete_scores = []
for ix, line in enumerate(myin):
    stack = []
    for token in line:
        if token in open_tokens:
            stack.append(token)
        elif token in close_tokens:
            if open_tokens.index(stack[-1]) == close_tokens.index(token):
                stack.pop()
            else:
                stack = []
                break
    score = 0
    while stack:
        token = stack.pop()
        score *= 5
        score += token_score_map[token]
    if score != 0:
        autocomplete_scores.append(score)
print(median(autocomplete_scores))
