redMax = 12
greenMax = 13
blueMax = 14

def parseGames(filePath):
    """
    >>> parseGames("sample1.txt")
    [{'gameId': 1, 'rounds': [[4, 0, 3], [1, 2, 6], [0, 2, 0]]}, {'gameId': 2, 'rounds': [[0, 2, 1], [1, 3, 4], [0, 1, 1]]}, {'gameId': 3, 'rounds': [[20, 8, 6], [4, 13, 5], [1, 5, 0]]}, {'gameId': 4, 'rounds': [[3, 1, 6], [6, 3, 0], [14, 3, 15]]}, {'gameId': 5, 'rounds': [[6, 3, 1], [1, 2, 2]]}]
    """
    with open(filePath, "r") as file:
        acc = []
        for line in file:
            content = line.split(":")
            gameNum = int(content[0].split(" ")[1])
            rounds = content[1].split(";")
            parsedRounds = []
            for round in rounds:
                sums = [0, 0, 0]
                cubes = round.split(",")
                for col in cubes:
                    info = col.strip().split(" ")
                    if info[1] == "red":
                        sums[0] = sums[0] + int(info[0])
                    elif info[1] == "green":
                        sums[1] = sums[1] + int(info[0])
                    elif info[1] == "blue":
                        sums[2] = sums[2] + int(info[0])
                parsedRounds.append(sums)
            acc.append({"gameId": gameNum, "rounds": parsedRounds})
        return acc

def gamePower(game):
    """
    >>> gamePower({'gameId': 11, 'rounds': [[0, 0, 0]]})
    0
    >>> gamePower({'gameId': 1, 'rounds': [[4, 0, 3], [1, 2, 6], [0, 2, 0]]})
    48
    >>> gamePower({'gameId': 1, 'rounds': [[0, 2, 1], [1, 3, 4], [0, 1, 1]]})
    12
    >>> gamePower({'gameId': 1, 'rounds': [[20, 8, 6], [4, 13, 5], [1, 5, 0]]})
    1560
    >>> gamePower({'gameId': 1, 'rounds': [[3, 1, 6], [6, 3, 0], [14, 3, 15]]})
    630
    >>> gamePower({'gameId': 1, 'rounds': [[6, 3, 1], [1, 2, 2]]})
    36
    """
    maxes = [0, 0, 0]
    result = 1
    for round in game["rounds"]:
        if round[0] > maxes[0]:
            maxes[0] = round[0]
        if round[1] > maxes[1]:
            maxes[1] = round[1]
        if round[2] > maxes[2]:
            maxes[2] = round[2]
    for num in maxes:
        result *= num
    return result
    
def solve(filePath):
    """
    >>> solve("sample1.txt")
    2286
    """
    games = parseGames(filePath)
    total = 0
    for game in games:
        total = total + gamePower(game)
    return total

result = solve("input.txt")
print("Sum of game power is:", result)