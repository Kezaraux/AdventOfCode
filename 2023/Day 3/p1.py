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

def solve(filePath):
    """
    >>> solve("sample1.txt")
    4361
    """
    grid = parseInput(filePath)
    symbols = getSymbolLocations(grid)
    hits = []
    for symbol in symbols:
        hits.extend(findHits(grid, symbol))
    filteredHits = set()
    for hit in hits:
        hitStart = getHitStart(grid, hit)
        if not hitStart in filteredHits:
            filteredHits.add(hitStart)
    numbers = []
    for hit in filteredHits:
        numbers.append(getNumFromHit(grid, hit))
    return sum(numbers)

result = solve("input.txt")
print("Total is:", result)
