actionToScore = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
def scoreRound(theirs, mine):
    theirs = actionToScore[theirs]
    mine = actionToScore[mine]
    if theirs == mine:
        # Draw
        return mine + 3
    if mine == (theirs + 1) or (mine == 1 and theirs == 3):
        # Win
        return mine + 6
    # Lose
    return mine + 0
myin = [scoreRound(*round.split()) for round in open("input.txt", "r").readlines()]
print(sum(myin))
