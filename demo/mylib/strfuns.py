# String function

def hasUpper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def countUpper(st):
    count = 0
    for c in st:
        if c.isupper():
           count += 1

    return count