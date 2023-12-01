import re

def indexOfAll(str, search):
    """Returns a list of all indices for the search term in the string

    >>> indexOfAll("one", "one")
    [0]
    >>> indexOfAll("twoneone", "one")
    [2, 5]
    """
    indices = []
    ind = str.find(search)
    while ind != -1:
        indices.append(ind)
        ind = str.find(search, indices[-1]+1)
    return indices

def getDigits(text):
    """Filter a string to only contain digits

    >>> getDigits("1abc2")
    '12'
    >>> getDigits("pqr3stu8vwx")
    '38'
    >>> getDigits("a1b2c3d4e5f")
    '12345'
    >>> getDigits("treb7uchet")
    '7'
    """
    return ''.join(c for c in text if c.isdigit())

def textToNum(line):
    """
    >>> textToNum("xtwone3fourone")
    '21341'
    """
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word2num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    thing = {}
    for word in words:
        thing[word] = indexOfAll(line, word)
    acc = ""
    for i in range(0, len(line)):
        indMatch = None
        vals = list(thing.values())
        for j in range(0,len(vals)):
            if i in vals[j]:
                indMatch = list(thing)[j]
        if indMatch == None:
            acc = acc + line[i]
        else:
            acc = acc + word2num[indMatch]
    return getDigits(acc)

def parseLine(line):
    """Parse a line for digits and return the first and last concatenated.
    
    >>> parseLine("1abc2")
    12
    >>> parseLine("pqr3stu8vwx")
    38
    >>> parseLine("a1b2c3d4e5f")
    15
    >>> parseLine("treb7uchet")
    77
    >>> parseLine("xtwone3four")
    24
    >>> parseLine("one")
    11
    >>> parseLine("two")
    22
    >>> parseLine("three")
    33
    >>> parseLine("four")
    44
    >>> parseLine("five")
    55
    >>> parseLine("six")
    66
    >>> parseLine("seven")
    77
    >>> parseLine("eight")
    88
    >>> parseLine("nine")
    99
    >>> parseLine("twone")
    21
    >>> parseLine("nineight")
    98
    >>> parseLine("fiveightwo")
    52
    """
    digits = getDigits(textToNum(line))
    first = digits[0]
    last = digits[-1]
    return int(first + last)

with open("input.txt", "r") as file:
    total = 0
    print("Starting...")
    for line in file:
        lineValue = parseLine(line)
        total = total + lineValue
    print("Done!")
    print("Total value is: ", total)