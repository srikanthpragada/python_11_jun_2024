with open("names.txt", "rt") as f:
    lines = f.readlines()

with  open("names.txt", "wt") as f:
    for line in lines:
        if len(line) > 1:  # line always contains \n so check for 2 chars
            f.write(line)
