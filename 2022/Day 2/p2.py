opponentMap = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
myMap = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}
moveToScore = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
victories = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
defeats = {"ROCK": "PAPER", "PAPER": "SCISSORS", "SCISSORS": "ROCK"}

def makeRPSTuple(line):
    """Converts a line of text into a tuple of rock paper scissors moves.

    >>> makeRPSTuple("A X")
    ('ROCK', 'LOSE')
    >>> makeRPSTuple("B X")
    ('PAPER', 'LOSE')
    >>> makeRPSTuple("C X")
    ('SCISSORS', 'LOSE')
    >>> makeRPSTuple("A Y")
    ('ROCK', 'DRAW')
    >>> makeRPSTuple("A Z")
    ('ROCK', 'WIN')
    """
    moves = line.split(" ")
    return (opponentMap[moves[0]], myMap[moves[1]])

def determineMove(moveTuple):
    """
    >>> determineMove(("ROCK", "WIN"))
    'PAPER'
    >>> determineMove(("SCISSORS", "DRAW"))
    'SCISSORS'
    """
    cpu = moveTuple[0]
    result = moveTuple[1]
    if result == "DRAW":
        return cpu
    elif result == "LOSE":
        return victories[cpu]
    else:
        return defeats[cpu]


def scoreGame(moveTuple):
    """
    >>> scoreGame(('ROCK', 'WIN'))
    8
    >>> scoreGame(('PAPER', 'LOSE'))
    1
    >>> scoreGame(('SCISSORS', 'DRAW'))
    6
    """
    cpu = moveTuple[0]
    player = determineMove(moveTuple)
    moveScore = moveToScore[player]
    defeats = victories[player]
    if cpu == player:
        return moveScore + 3
    elif cpu in defeats:
        return moveScore + 6
    else:
        return moveScore

with open("input.txt", "r") as file:
    score = 0
    for line in file:
        moves = makeRPSTuple(line.strip())
        score = score + scoreGame(moves)
    print("Total score: ", score)