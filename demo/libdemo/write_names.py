
names = ['Larry', 'Scott', 'Tom','Richards', 'Mark', 'Gladwell']

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()
