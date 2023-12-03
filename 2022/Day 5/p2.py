def readRow(row):
    """
    >>> readRow("    [A]    ")
    [None, 'A', None]
    >>> readRow("[M] [H]         [N]                ")
    ['M', 'H', None, None, 'N', None, None, None, None]
    >>> readRow("[R] [P] [W] [N] [M] [P] [R] [Q] [L]")
    ['R', 'P', 'W', 'N', 'M', 'P', 'R', 'Q', 'L']
    """
    acc = []
    for i in range(1, len(row), 4):
        if row[i] == " ":
            acc.append(None)
        else:
            acc.append(row[i])
    return acc

def readInstruction(instruction):
    """
    >>> readInstruction("move 1 from 2 to 1")
    {'amount': 1, 'source': 2, 'dest': 1}
    >>> readInstruction("move 11 from 4 to 1")
    {'amount': 11, 'source': 4, 'dest': 1}
    """
    parsed = instruction.split(" ")
    return {"amount": int(parsed[1]), "source": int(parsed[3]), "dest": int(parsed[5])}

def convertToColumns(state):
    """
    >>> convertToColumns([[None, 'D', None], ['N', 'C', None], ['Z', 'M', 'P']])
    [[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P']]
    """
    return [list(x) for x in zip(*state)]

def parseInput(filePath):
    """
    >>> parseInput("sample1.txt")
    {'state': [[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P']], 'instructions': [{'amount': 1, 'source': 2, 'dest': 1}, {'amount': 3, 'source': 1, 'dest': 3}, {'amount': 2, 'source': 2, 'dest': 1}, {'amount': 1, 'source': 1, 'dest': 2}]}
    """
    with open(filePath, "r") as file:
        content = file.read()
        info = content.split("\n\n")
        state = info[0].split("\n")
        instructions = info[1].strip().split("\n")

        rows = [readRow(row) for row in state[0:-1]]
        parsed = [readInstruction(instruction) for instruction in instructions]
        return {"state": convertToColumns(rows), "instructions": parsed}
        
def simpleMove(colA, colB, amount):
    """
    >>> simpleMove([None, 'W', 'S', 'L', 'G', 'N', 'T', 'R'], [None, None, None, None, 'W', 'M', 'R', 'P'], 1)
    [[None, None, 'S', 'L', 'G', 'N', 'T', 'R'], [None, None, None, 'W', 'W', 'M', 'R', 'P']]
    >>> simpleMove([None, 'A', 'B'], ['C', 'D', 'E'], 2)
    [[None, None, None, None, None], ['A', 'B', 'C', 'D', 'E']]
    """
    listLen = len(colA)
    cleanA = list(filter(None, colA))
    cleanB = list(filter(None, colB))

    toMove = min(amount, len(cleanA))
    movedItems = cleanA[0:toMove]
    cleanA = cleanA[toMove:]
    cleanB = movedItems + cleanB

    listLen = max(listLen, len(cleanA), len(cleanB))

    diffA = abs(listLen - len(cleanA))
    diffB = abs(listLen - len(cleanB))
    cleanA = ([None] * diffA) + cleanA
    cleanB = ([None] * diffB) + cleanB
    return [cleanA, cleanB]



def move(state, instruction):
    """
    >>> move([[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P']], {'amount': 2, 'source': 1, 'dest': 2})
    [[None, None, None, None, None], ['N', 'Z', 'D', 'C', 'M'], [None, None, None, None, 'P']]
    >>> move([[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P']], {'amount': 1, 'source': 2, 'dest': 1})
    [['D', 'N', 'Z'], [None, 'C', 'M'], [None, None, 'P']]
    >>> move(parseInput("input.txt")["state"], {'amount': 1, 'source': 7, 'dest': 6})
    [['M', 'S', 'J', 'L', 'V', 'F', 'N', 'R'], ['H', 'W', 'J', 'F', 'Z', 'D', 'N', 'P'], [None, None, None, 'G', 'D', 'C', 'R', 'W'], [None, None, None, None, None, 'S', 'B', 'N'], ['N', 'F', 'B', 'C', 'P', 'W', 'Z', 'M'], [None, None, None, 'W', 'W', 'M', 'R', 'P'], [None, None, 'S', 'L', 'G', 'N', 'T', 'R'], [None, 'V', 'B', 'N', 'F', 'H', 'T', 'Q'], [None, None, 'F', 'N', 'Z', 'H', 'M', 'L']]
    """
    # Offset source/dest to get proper indices
    source = instruction["source"] - 1
    dest = instruction["dest"] - 1
    amount = instruction["amount"]

    newState = state
    newRows = simpleMove(state[source], state[dest], amount)
    newState[source] = newRows[0]
    newState[dest] = newRows[1]
    newListLen = len(newRows[0])
    for i in range(0, len(newState)):
        if len(newState[i]) != newListLen:
            newState[i] = ([None] * (newListLen - len(newState[i]))) + newState[i]
    return newState

def readTopCrates(state):
    """
    >>> readTopCrates([[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P']])
    'NDP'
    >>> readTopCrates([[None, 'N', 'Z'], ['D', 'C', 'M'], [None, None, 'P'], [None, None, None]])
    'NDP'
    >>> readTopCrates(parseInput("input.txt")["state"])
    'MHGSNWWVF'
    """
    cleaned = [list(filter(None, col)) for col in state]
    acc = []
    for i in range(len(cleaned)):
        acc.append(next(iter(cleaned[i]), ''))
    return ''.join(acc)

def solve(filePath):
    """
    >>> solve("sample1.txt")
    'MCD'
    """
    parsed = parseInput(filePath)
    state = parsed["state"]
    instructions = parsed["instructions"]

    for instruction in instructions:
        state = move(state, instruction)
    return readTopCrates(state)

result = solve("input.txt")
print("Top crates are:", result)