# Remove excessive spaces and new lines 
import re

with open("test.txt", "rt") as f:
    contents = f.read()

contents = re.sub(' +', ' ', contents)
contents = re.sub('\n+', '\n', contents)

with open("test.txt", "wt") as f:
    f.write(contents)


