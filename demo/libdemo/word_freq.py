import re

with open("story.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for word in sorted(set(words)):
    print(f"{word:15} - {words.count(word)}")
