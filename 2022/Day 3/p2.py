alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getGroups(filePath):
    """
    >>> getGroups("sample1.txt")
    [['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'], ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']]
    """
    with open(filePath, "r") as file:
        lines = file.readlines()
        groups = [line.strip() for line in lines]
        groupSize = 3
        return [groups[i:i+groupSize] for i in range(0, len(groups), groupSize)]
    
def findDupeGroup(group):
    """
    >>> findDupeGroup(['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'])
    'r'
    >>> findDupeGroup(['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw'])
    'Z'
    """
    intersection = set(group[0]).intersection(group[1]).intersection(group[2])
    return list(intersection)[0]

def getLetterPriority(letter):
    """
    >>> getLetterPriority("a")
    1
    >>> getLetterPriority("z")
    26
    >>> getLetterPriority("A")
    27
    >>> getLetterPriority("Z")
    52
    """
    return alphabet.index(letter) + 1

groups = getGroups("input.txt")
dupes = [findDupeGroup(group) for group in groups]
prios = [getLetterPriority(group) for group in dupes]
prioSum = sum(prios)

print("The sum of the priorities is: ", prioSum)
