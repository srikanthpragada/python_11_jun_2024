
fs = "java"
ss = "javascript"

found = ""
for c in fs:
    if c in ss and c not in found:
        print(c)
        found = found + c

