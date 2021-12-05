myin = open("input.txt", "r").read().split("\n\n")
draw_numbers = list(map(int, myin[0].split(',')))
boards = [[list(map(int, line.split())) for line in board.split('\n')] for board in myin[1:]]
winners = set()
for num in draw_numbers:
    for (ix, board) in enumerate(boards):
        if ix not in winners:
            boards[ix] = [[-1 if num == board_num else board_num for board_num in line] for line in board]
            row_win = any(list(map(lambda line: all(board_num == -1 for board_num in line), boards[ix])))
            col_win = any(list(map(lambda line: all(board_num == -1 for board_num in line), list(zip(*boards[ix])))))
            if row_win or col_win:
                winners.add(ix)
                if len(winners) == len(boards):
                    print(sum(list(map(lambda line: sum([board_num if board_num != -1 else 0 for board_num in line]), boards[ix]))) * num)
