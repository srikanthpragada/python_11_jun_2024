import re

with open("clients.txt", "rt") as f:
    for line in f.readlines():
        m = re.search(r"\d+", line)
        if m is not None:
            if len(m.group()) == 10:
                print(m.group())


