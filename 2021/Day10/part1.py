myin = [line.replace('\n', '') for line in open("input.txt", "r").readlines()]
open_tokens = '[({<'
close_tokens = '])}>'
token_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
syntax_error_score = 0
for line in myin:
    stack = []
    for token in line:
        if token in open_tokens:
            stack.append(token)
        elif token in close_tokens:
            if open_tokens.index(stack[-1]) == close_tokens.index(token):
                stack.pop()
            else:
                syntax_error_score += token_score_map[token]
                break
print(syntax_error_score)
