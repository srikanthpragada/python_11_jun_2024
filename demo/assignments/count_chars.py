def count_chars(st, ch=' ', spos=0):
    return st[spos:].count(ch)


print(count_chars('Hello', 'l'))
print(count_chars('how are you'))
