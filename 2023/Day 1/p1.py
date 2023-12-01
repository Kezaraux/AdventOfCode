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
    """
    digits = getDigits(line)
    first = digits[0]
    last = digits[-1]
    return int(first + last)


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

with open("input.txt", "r") as file:
    total = 0
    print("Starting...")
    for line in file:
        total = total + parseLine(line)
    print("Done!")
    print("Total value is: ", total)
