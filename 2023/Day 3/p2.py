def parseInput(filePath):
    """
    >>> parseInput("sample1.txt")
    ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']
    """
    with open(filePath, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]
    
def getSymbolLocations(grid):
    """
    >>> getSymbolLocations(parseInput("sample1.txt"))
    [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]
    """
    acc = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if not grid[i][j].isdigit() and grid[i][j] != '.':
                acc.append((i, j))
    return acc

def getPotentialGearLocations(grid, hits):
    """
    >>> getPotentialGearLocations(parseInput("sample1.txt"), [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)])
    [(1, 3), (4, 3), (8, 5)]
    """
    acc = []
    for hit in hits:
        symbol = grid[hit[0]][hit[1]]
        if symbol == '*':
            acc.append(hit)
    return acc


def findHits(grid, coord):
    """
    >>> findHits(['467..114..', '...*......', '..35..633.'], (1,3))
    [(0, 2), (2, 2), (2, 3)]
    >>> findHits(['......755.', '...$.*....', '.664.598..'], (1,3))
    [(2, 2), (2, 3)]
    """
    acc = []
    top = max(0, coord[0]-1)
    bottom = min(len(grid), coord[0]+1)+1
    for i in range(top, bottom):
        left = max(0, coord[1]-1)
        right = min(len(grid[i]), coord[1]+1)+1
        for j in range(left, right):
            if grid[i][j].isdigit():
                acc.append((i, j))
    return acc

def getNumFromHit(grid, coord):
    """
    >>> getNumFromHit(['467..114..', '...*......', '..35..633.'], (0,2))
    467
    >>> getNumFromHit(['467..114..', '...*......', '..35..633.'], (2,2))
    35
    >>> getNumFromHit(['467..114..', '...*......', '..35..633.'], (2,3))
    35
    """
    start = 0
    row = grid[coord[0]]
    end = len(row)
    for i in range(coord[1], -1, -1):
        if not row[i].isdigit():
            start = i+1
            break
    for i in range(coord[1], end):
        if not row[i].isdigit():
            end = i
            break
    return int(row[start:end])

def getHitStart(grid, hit):
    """
    >>> getHitStart(['467..114..'], (0, 2))
    (0, 0)
    >>> getHitStart(['..35..633.'], (0,3))
    (0, 2)
    >>> getHitStart(['..35..633.'], (0,2))
    (0, 2)
    """
    start = 0
    row = grid[hit[0]]
    for i in range(hit[1], -1, -1):
        if not row[i].isdigit():
            start = i+1
            break
    return (hit[0], start)

def checkPotentialGear(grid, gearHit):
    """
    >>> checkPotentialGear(parseInput("sample1.txt"), (1,3))
    16345
    >>> checkPotentialGear(parseInput("sample1.txt"), (4,3))
    0
    >>> checkPotentialGear(parseInput("sample1.txt"), (8,5))
    451490
    """
    allHits = findHits(grid, gearHit)
    filtered = set()
    for hit in allHits:
        hitStart = getHitStart(grid, hit)
        if not hitStart in filtered:
            filtered.add(hitStart)
    if len(filtered) == 2:
        nums = []
        for hit in filtered:
            nums.append(getNumFromHit(grid, hit))
        return nums[0] * nums[1]
    else:
        return 0
    
def solve(filePath):
    """
    >>> solve("sample1.txt")
    467835
    """
    grid = parseInput(filePath)
    symbols = getSymbolLocations(grid)
    potentialGears = getPotentialGearLocations(grid, symbols)
    total = 0
    for gear in potentialGears:
        total = total + checkPotentialGear(grid, gear)
    return total

result = solve("input.txt")
print("Total is:", result)