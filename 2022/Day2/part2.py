actionToScore = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
def scoreRound(theirs, mine):
    outcomeScore = actionToScore[mine]
    if mine == 'Y':
        # Draw
        return actionToScore[theirs] + outcomeScore
    if mine == 'X':
        # Lose
        actionScore = actionToScore[theirs] - 1 if theirs != 'A' else 3
        return actionScore + outcomeScore
    if mine == 'Z':
        # Win
        actionScore = actionToScore[theirs] + 1 if theirs != 'C' else 1
        return actionScore + outcomeScore

myin = [scoreRound(*round.split()) for round in open("input.txt", "r").readlines()]
print(sum(myin))
