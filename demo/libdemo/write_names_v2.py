names = ['Larry', 'Scott', 'Tom', 'Richards', 'Mark', 'Gladwell']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")
