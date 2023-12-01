opponentMap = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
myMap = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
moveToScore = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
victories = {"ROCK": ["SCISSORS"], "PAPER": ["ROCK"], "SCISSORS": ["PAPER"]}

def makeRPSTuple(line):
    """Converts a line of text into a tuple of rock paper scissors moves.

    >>> makeRPSTuple("A X")
    ('ROCK', 'ROCK')
    >>> makeRPSTuple("B X")
    ('PAPER', 'ROCK')
    >>> makeRPSTuple("C X")
    ('SCISSORS', 'ROCK')
    >>> makeRPSTuple("A Y")
    ('ROCK', 'PAPER')
    >>> makeRPSTuple("A Z")
    ('ROCK', 'SCISSORS')
    """
    moves = line.split(" ")
    return (opponentMap[moves[0]], myMap[moves[1]])

def scoreGame(moveTuple):
    """
    >>> scoreGame(('ROCK', 'PAPER'))
    8
    >>> scoreGame(('PAPER', 'ROCK'))
    1
    >>> scoreGame(('SCISSORS', 'SCISSORS'))
    6
    """
    cpu = moveTuple[0]
    player = moveTuple[1]
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