
f = open("names.txt", "rt")

for name in sorted(f.readlines()):
    print(name.strip())

f.close()

