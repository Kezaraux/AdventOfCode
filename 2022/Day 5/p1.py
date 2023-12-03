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

def parseInput(filePath):
    """
    >>> parseInput("sample1.txt")
    {'state': [[None, 'D', None], ['N', 'C', None], ['Z', 'M', 'P']], 'instructions': [{'amount': 1, 'source': 2, 'dest': 1}, {'amount': 3, 'source': 1, 'dest': 3}, {'amount': 2, 'source': 2, 'dest': 1}, {'amount': 1, 'source': 1, 'dest': 2}]}
    """
    with open(filePath, "r") as file:
        content = file.read()
        info = content.split("\n\n")
        state = info[0].split("\n")
        instructions = info[1].strip().split("\n")

        rows = [readRow(row) for row in state[0:-1]]
        parsed = [readInstruction(instruction) for instruction in instructions]
        return {"state": rows, "instructions": parsed}
        
def move(state, source, dest):
    """
    >>> move([[None, 'D', None], ['N', 'C', None], ['Z', 'M', 'P']], 1, 3)
    [[None, 'D', None], [None, 'C', 'N'], ['Z', 'M', 'P']]
    >>> move([[None, 'D', None], ['N', 'C', None], ['Z', 'M', 'P']], 1, 2)
    [[None, 'N', None], [None, 'D', None], [None, 'C', None], ['Z', 'M', 'P']]
    """
    # Offset source/dest to get proper indices
    source -= 1
    dest -= 1

    sourceRow = -1
    destRow = -1
    newState = state
    for i in range(0, len(state)):
        if state[i][source] != None:
            sourceRow = i
            break
    for i in range(len(state)-1, -1, -1):
        if state[i][dest] == None:
            destRow = i
            break
    if destRow == -1:
        newRow = [None] * len(state[0])
        newState = [newRow] + newState
        destRow = 0
        sourceRow += 1
    newState[sourceRow][source], newState[destRow][dest] = newState[destRow][dest], newState[sourceRow][source]
    return newState

def readTopCrates(state):
    """
    >>> readTopCrates([[None, 'D', None], ['N', 'C', None], ['Z', 'M', 'P']])
    'NDP'
    >>> readTopCrates([[None, 'D', None, None], ['N', 'C', None, None], ['Z', 'M', 'P', None]])
    'NDP'
    >>> readTopCrates(parseInput("input.txt")["state"])
    'MHGSNWWVF'
    """
    acc = [" "] * len(state[0])
    for i in range(0, len(state)):
        for j in range(len(state[0])):
            if state[i][j] != None and acc[j] == " ":
                acc[j] = state[i][j]
    return ''.join(acc).strip()

def solve(filePath):
    """
    >>> solve("sample1.txt")
    'CMZ'
    """
    parsed = parseInput(filePath)
    state = parsed["state"]
    instructions = parsed["instructions"]

    for instruction in instructions:
        for i in range(0, instruction["amount"]):
            state = move(state, instruction["source"], instruction["dest"])

    return readTopCrates(state)

result = solve("input.txt")
print("Top crates are:", result)