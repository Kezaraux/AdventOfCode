def parseInput(filePath):
    """
    >>> parseInput("sample1.txt")
    [[[2, 4], [6, 8]], [[2, 3], [4, 5]], [[5, 7], [7, 9]], [[2, 8], [3, 7]], [[6, 6], [4, 6]], [[2, 6], [4, 8]]]
    """
    with open(filePath, "r") as file:
        lines = file.readlines()
        cleaned = [line.strip() for line in lines]
        acc = []
        for line in cleaned:
            pairs = line.split(",")
            parsed = [[int(val) for val in pair.split("-")] for pair in pairs]
            acc.append(parsed)
        return acc
    
def getSetFromRange(val):
    """
    >>> getSetFromRange([2, 4])
    {2, 3, 4}
    >>> getSetFromRange([1, 9])
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    """
    return set(range(val[0], val[1]+1))

def checkSetOverlap(setA, setB):
    """
    >>> checkSetOverlap({1, 2, 3}, {3, 4, 5})
    True
    >>> checkSetOverlap({1, 2, 3}, {4, 5})
    False
    """
    return len(setA.intersection(setB)) > 0

def solve(filePath):
    """
    >>> solve("sample1.txt")
    2
    """
    pairs = parseInput(filePath)
    total = 0
    for pair in pairs:
        setA = getSetFromRange(pair[0])
        setB = getSetFromRange(pair[1])
        if checkSetOverlap(setA, setB):
            total += 1
    return total

result = solve("input.txt")
print("Total is:", result)