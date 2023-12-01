def getGroups(filePath):
    """Opens a file, reads contents, and returns a list of groups.

    >>> getGroups("sample1.txt")
    [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    """
    with open(filePath, "r") as file:
        content = file.read()
        groups = content.split("\n\n")
        parsed = [group.split("\n") for group in groups]
        cleaned = [list(filter(lambda x: x != "", group)) for group in parsed]
        return [list(map(int, group)) for group in cleaned]
    
def findMaxByKeyGroup(groups, key):
    """Returns the index of the group with the max sum, and that sum.
    
    >>> findMaxByKeyGroup([[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]], "sum")
    {'index': 3, 'sum': 24000, 'items': 3, 'largestItem': 9000}
    >>> findMaxByKeyGroup([[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]], "largestItem")
    {'index': 4, 'sum': 10000, 'items': 1, 'largestItem': 10000}
    >>> findMaxByKeyGroup([[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]], "items")
    {'index': 3, 'sum': 24000, 'items': 3, 'largestItem': 9000}
    """
    groupDicts = [groupToDict(group, ind) for ind, group in enumerate(groups)]
    maxGroup = max(groupDicts, key=lambda x: x[key])
    return maxGroup

def groupToDict(group, index):
    """Converts an array of strings into a group dictionary.
    
    >>> groupToDict([1000, 2000, 3000], 0)
    {'index': 0, 'sum': 6000, 'items': 3, 'largestItem': 3000}
    """
    return { "index": index, "sum": sum(group), "items": len(group), "largestItem": max(group) }

parsedGroups = getGroups("input.txt")
result = findMaxByKeyGroup(parsedGroups, "sum")
print("Largest group for key is: ", result)
del parsedGroups[result["index"]]
result2 = findMaxByKeyGroup(parsedGroups, "sum")
print("Second largest group is: ", result2)
del parsedGroups[result2["index"]]
result3 = findMaxByKeyGroup(parsedGroups, "sum")
print("Third largest group: ", result3)

total3 = result["sum"] + result2["sum"] + result3["sum"]
print("Their sum is: ", total3)