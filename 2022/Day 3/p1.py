alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getGroups(filePath):
    """
    >>> getGroups("sample1.txt")
    ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
    """
    with open(filePath, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]
    
def findDupe(group):
    """Splits the given string group in half and finds the first character
    shared between the two subgroups

    >>> findDupe("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    >>> findDupe("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    'L'
    >>> findDupe("PmmdzqPrVvPwwTWBwg")
    'P'
    >>> findDupe("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    'v'
    >>> findDupe("ttgJtRGJQctTZtZT")
    't'
    >>> findDupe("CrZsJsPPZsGzwwsLwLmpwMDw")
    's'
    """
    first = None
    second = None
    n = len(group)
    if n % 2 == 0:
        first = set(group[0:n//2])
        second = set(group[n//2:])
    else:
        first = set(group[0:(n//2+1)])
        second = set(group[(n//2+1):])
    intersection = list(first.intersection(second))
    return intersection[0]

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
dupes = [findDupe(group) for group in groups]
prios = [getLetterPriority(group) for group in dupes]
prioSum = sum(prios)

print("The sum of the priorities is: ", prioSum)
